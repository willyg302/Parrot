import facebook
import json

tokens = None

with open('tokens.txt', 'r') as f:
	tokens = json.loads(f.read())

if tokens is not None:
	graph = facebook.GraphAPI(tokens['fb_token'])
	print graph.get_object('barackobama/feed')