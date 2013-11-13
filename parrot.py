import sys, argparse, json

import facebook
from twython import Twython

tokens = None

# Returns True if tokens successfully loaded
def load_tokens(mode):
	global tokens # Needed to modify global variable "tokens"
	try:
		with open('tokens.json', 'r') as f:
			tokens = json.load(f)[mode]
		return True
	except IOError, ValueError:
		print 'Error loading authorization tokens!'
		return False

# Parrot is being run directly from CLI
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--debug", help="set Parrot to debug mode", action="store_true")
	args = parser.parse_args()
	if not load_tokens('debug' if args.debug else 'production'):
		sys.exit(1)

	# Example: get Facebook feed of Obama
	#graph = facebook.GraphAPI(tokens['fb_token'])
	#print graph.get_object('barackobama/feed')

if __name__ == "__main__":
	main()