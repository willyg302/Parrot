import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.web

import hashlib

import parrot_settings
import tokens

from tornado import gen
from tornado.options import define, options, parse_command_line
from tornado.log import app_log


# Tornado settings (we default to run on port 8888)
define('port', default=8888, help="The port to run Parrot on", type=int)


class Application(tornado.web.Application):

	def __init__(self):
		handlers = [
			(r'/', MainHandler),
			(r'/login', LoginHandler),
			(r'/logout', LogoutHandler),
		]
		settings = dict(
			template_path=parrot_settings.TEMPLATE_PATH,
			static_path=parrot_settings.STATIC_PATH,
			debug=parrot_settings.DEBUG,
			cookie_secret=tokens.COOKIE_SECRET,
			login_url='/login',
		)
		tornado.web.Application.__init__(self, handlers, **settings)


class BaseHandler(tornado.web.RequestHandler):

	def get_current_user(self):
		return self.get_secure_cookie('parrot_user')

	def get_login_url(self):
		return u"/login"


class MainHandler(BaseHandler):

	@tornado.web.authenticated
	def get(self):
		username = tornado.escape.xhtml_escape(self.current_user)
		self.render('index.html', username=username)


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
		app_log.info("User {0} logging in with password {1}".format(username, password))
		if self.check_permission(username, password):
			self.set_current_user(username)
			self.redirect(self.get_argument('next', u'/'))
		else:
			error_msg = u"?error=" + tornado.escape.url_escape("Login incorrect")
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
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
	main()