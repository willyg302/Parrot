from log import parrot_log


class Kernel:
	def __init__(self):
		pass

	def handle_input(self, string):
		parrot_log.info(string)
		return string + "woo"