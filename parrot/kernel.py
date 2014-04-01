import shlex

from logger import log
from _docopt import docopt


class Command:
	registry = {}
	short_docs = []

	def __init__(self, doc=None):
		Command.short_docs.append(doc)

	def __call__(self, f):
		Command.registry[f.func_name] = f
		def wrapped_f(self, args):
			arguments = docopt(f.__doc__, argv=args)
			if not arguments:
				return 'Argument error!'
			return f(self, arguments)
		return wrapped_f

	@classmethod
	def list(self):
		ret = '<b>Unrecognized command!</b>\n\nAvailable commands:\n'
		for f, short_doc in zip(Command.registry, Command.short_docs):
			ret += '  {}{}\n'.format(f, (" : " + short_doc) if short_doc else '')
		return ret


class Kernel:
	def __init__(self):
		pass

	@Command('Test function to make sure everything works')
	def test(self, args):
		"""
		Usage: test [-h | --help] (ODD EVEN)...

		Example, try:
		  test 1 2 3 4

		Options:
		  -h, --help
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
		return Command.list()  # Unrecognized command, show list of known commands

	def handle_input(self, string):
		log.info('Servicing request: {}'.format(string))
		raw_cmd = shlex.split(string)
		return str(self.runCommand(raw_cmd[0], raw_cmd[1:])).replace('\n', '<br>').replace(' ', '&nbsp;')