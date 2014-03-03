import logging


class Kernel:
	def __init__(self):
		pass

	def handle_input(self, string):
		logging.info(string)
		return string + "woo"