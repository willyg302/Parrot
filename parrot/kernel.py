import shlex

from tornado.template import Template

import parrot_settings
from logger import log
from _docopt import docopt


list_html = """<b style="color: red;">Unrecognized command "{{ unrecognized }}"</b>

Available commands:
{% for f, short_doc in commands %}  <b>{{ '{: <10}'.format(f) }}</b>{% if short_doc %}{{ short_doc }}{% end %}
{% end %}
"""

malformed_html = """<b style="color: red;">Parrot could not understand your input "{{ command }} {{ args }}"</b>

Need help?
<ul><li>Type "{{ command }} -h"</li><li>Visit the <a href="/help">Help page</a></li></ul>
"""


class Command:
	registry = []
	short_docs = []

	def __init__(self, doc=None):
		Command.short_docs.append(doc)

	def __call__(self, f):
		Command.registry.append(f.func_name)
		def wrapped_f(self, args):
			arguments = docopt(f.__doc__, argv=args)
			if not arguments:
				return Template(malformed_html).generate(command=f.func_name, args=' '.join(args))
			return f(self, arguments)
		return wrapped_f

	@classmethod
	def list(self, unrecognized):
		return Template(list_html).generate(unrecognized=unrecognized, commands=zip(Command.registry, Command.short_docs))


class Kernel:
	def __init__(self):
		pass

	# From Twitterator: ['Add user', 'Create database', 'Export', 'Search', 'Track keyword', 'Track user'];

	@Command('Search for a given keyword')
	def search(self, args):
		"""
		Usage:
		  search [-fty] <keyword>
		  search -h | --help

		Options:
		  -h --help      Show this help message.
		  -f --facebook  Search for keyword on Facebook.
		  -t --twitter   Search for keyword on Twitter.
		  -y --youtube   Search for keyword on YouTube.
		"""

		# Example args information:
		# {'--facebook': False,
		# '--help': False,
		# '--twitter': True,
		# '--youtube': False,
		# '': 'f'}



		return str(args)

	@Command('Test function to make sure everything works')
	def test(self, args):
		"""
		Usage: test [-h | --help] (ODD EVEN)...

		Example, try:
		  test 1 2 3 4

		Options:
		  -h --help      Show this help message.
		"""
		return str(args)

	@Command('Track a given keyword')
	def track(self, args):
		"""
		Usage:
		  track [-fty] <keyword>
		  track -h | --help

		Options:
		  -h --help      Show this help message.
		  -f --facebook  Track keyword on Facebook.
		  -t --twitter   Track keyword on Twitter.
		  -y --youtube   Track keyword on YouTube.
		"""
		return str(args)

	def runCommand(self, command, args):
		c = self.__class__
		if hasattr(c, command) and callable(getattr(c, command)):
			return getattr(c, command)(self, args)
		return Command.list(command)  # Unrecognized command, show list of known commands

	def handle_input(self, string):
		log.info('Servicing request: {}'.format(string))
		raw_cmd = shlex.split(string)
		return self.runCommand(raw_cmd[0], raw_cmd[1:])