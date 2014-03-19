import shlex

from logger import log
from _docopt import docopt


commands = {
	'test': """Usage: odd_even_example.py [-h | --help] (ODD EVEN)...

Example, try:
  odd_even_example.py 1 2 3 4

Options:
  -h, --help

"""
}


class Kernel:
	def __init__(self):
		pass

	def runCommand(self, command, args):
		if command not in commands:
			return 'Command not recognized!'
		arguments = docopt(commands[command], argv=args)
		if not arguments:
			return 'Argument error!'
		return arguments

	def handle_input(self, string):
		log.info('Servicing request: {}'.format(string))
		raw_cmd = shlex.split(string)
		return self.runCommand(raw_cmd[0], raw_cmd[1:])