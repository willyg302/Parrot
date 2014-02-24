import hashlib
import signal
import time
import logging

from tornado import escape, httpserver, ioloop, web
from tornado.options import define, options, parse_command_line

import parrot_settings
import tokens
from kernel import Kernel


# Tornado settings (we default to run on port 8888)
define('port', default=8888, help="The port to run Parrot on", type=int)


kernel = Kernel()


# Handle signals from the shell (or kill -9's)
def sig_handler(sig, frame):
	ioloop.IOLoop.instance().add_callback(shutdown)

# Graceful shutdown of the server
def shutdown():
	http_server.stop()
	io_loop = ioloop.IOLoop.instance()
	deadline = time.time() + parrot_settings.MAX_WAIT_SECONDS_BEFORE_SHUTDOWN

	def stop_loop():
		now = time.time()
		if now < deadline and (io_loop._callbacks or io_loop._timeouts):
			io_loop.add_timeout(now + 1, stop_loop)
		else:
			io_loop.stop()

	stop_loop()


class Application(web.Application):

	def __init__(self):
		handlers = [
			(r'/', MainHandler),
			(r'/login', LoginHandler),
			(r'/logout', LogoutHandler),
			(r'/search', InputHandler),
		]
		settings = dict(
			template_path=parrot_settings.TEMPLATE_PATH,
			static_path=parrot_settings.STATIC_PATH,
			debug=parrot_settings.DEBUG,
			cookie_secret=tokens.COOKIE_SECRET,
			login_url='/login',
		)
		web.Application.__init__(self, handlers, **settings)


class BaseHandler(web.RequestHandler):

	def get_current_user(self):
		return self.get_secure_cookie('parrot_user')

	def get_login_url(self):
		return u"/login"


class MainHandler(BaseHandler):

	@web.authenticated
	def get(self):
		username = escape.xhtml_escape(self.current_user)
		current = []
		historical = []
		self.render('index.html', username=username, current=current, historical=historical)


class InputHandler(BaseHandler):

	@web.authenticated
	def post(self):
		string = self.get_argument('data', '')
		response = kernel.handle_input(string)
		self.write(response)


class LoginHandler(BaseHandler):

	def get(self):
		errormessage = self.get_argument('error', '')
		self.render('login.html', errormessage=errormessage)

	def sha(self, data):
		return hashlib.sha256(repr(data) + tokens.COOKIE_SECRET).hexdigest()

	def check_permission(self, username, password):
		if username in parrot_settings.USER_DICT:
			if self.sha(password) == parrot_settings.USER_DICT[username]:
				return True
		return False

	def post(self):
		username = self.get_argument('username', '')
		password = self.get_argument('password', '')
		logging.info("User {0} logging in with password {1}".format(username, password))
		if self.check_permission(username, password):
			self.set_current_user(username)
			self.redirect(self.get_argument('next', u'/'))
		else:
			error_msg = u"?error=" + escape.url_escape("Login incorrect")
			self.redirect(u"/login" + error_msg)

	def set_current_user(self, user):
		if user:
			self.set_secure_cookie("parrot_user", user)
		else:
			self.clear_cookie("parrot_user")


class LogoutHandler(BaseHandler):

	def get(self):
		self.clear_cookie('parrot_user')
		self.redirect(self.get_argument('next', '/'))


# Logic if the app is being invoked directly
def main():
	parse_command_line()

	global http_server

	http_server = httpserver.HTTPServer(Application())
	http_server.listen(options.port)

	signal.signal(signal.SIGTERM, sig_handler)
	signal.signal(signal.SIGINT, sig_handler)

	ioloop.IOLoop.instance().start()


if __name__ == "__main__":
	main()