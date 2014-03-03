from logger import log


class Kernel:
	def __init__(self):
		pass

	def handle_input(self, string):
		log.info(string)
		return string + "woo"