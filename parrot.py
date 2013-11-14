import sys, argparse, json, logging, threading, Queue

import facebook
from twython import Twython

tokens = None

APP_NAME = 'Parrot'
VERSION = '0.1'

def user_input(q, lock):
	while True:
		with lock:
			cmd = raw_input()
		q.put(cmd)
		if cmd.lower() == 'exit':
			break

def handle_input(cmd, lock):
	print 'Received command: ' + cmd

def init_log(debug, flush):
	# Set up our basic file logger
	logging.basicConfig(
		level=(logging.DEBUG if debug else logging.INFO),
		filename='{}-log.log'.format(APP_NAME),
		filemode=('w' if flush else 'a'),
		format='%(asctime)s %(name)-12s %(levelname)-10s %(message)s',
		datefmt='%m-%d %H:%M')

	# Define an equivalent console logger
	console = logging.StreamHandler()
	console.setLevel(logging.INFO)
	console.setFormatter(logging.Formatter('%(name)-12s: %(levelname)-10s %(message)s'))
	logging.getLogger('').addHandler(console)

# Returns True if tokens successfully loaded
def load_tokens(mode):
	global tokens # Needed to modify global variable "tokens"
	try:
		with open('tokens.json', 'r') as f:
			tokens = json.load(f)[mode]
		return True
	except IOError, ValueError:
		logging.critical('Could not load authorization tokens!')
		return False

def exit():
	logging.info('{} exiting...'.format(APP_NAME))
	logging.info('-' * 40 + '\n')
	logging.shutdown()
	sys.exit(0)

# Parrot is being run directly from CLI
def main():

	# Parse command line arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--debug", help="set {} to debug mode".format(APP_NAME), action="store_true")
	parser.add_argument("-f", "--flush", help="flush the log file rather than appending", action="store_true")
	args = parser.parse_args()

	# Start our log
	init_log(args.debug, args.flush)
	logging.info('-' * 40)
	logging.info('{} starting up...'.format(APP_NAME))

	# Load our authorization tokens
	if not load_tokens('debug' if args.debug else 'production'):
		sys.exit(1)

	logging.info('{} v{} is up and running'.format(APP_NAME, VERSION))
	logging.info('-' * 40 + '\n')

	# Our main loop, we spawn a user input thread and associated queues/locks
	input_queue = Queue.Queue()
	input_lock = threading.Lock()
	threading.Thread(target=user_input, args=(input_queue, input_lock)).start()
	while True:
		cmd = input_queue.get()
		if cmd.lower() == 'exit':
			break
		handle_input(cmd, input_lock)

	# Since we are out of the loop, we are free to exit
	exit()

	# Example: get Facebook feed of Obama
	#graph = facebook.GraphAPI(tokens['fb_token'])
	#print graph.get_object('barackobama/feed')

if __name__ == "__main__":
	main()