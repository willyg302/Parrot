import os

project = 'Parrot'

TOKENS_FILE = os.path.join('parrot', 'tokens.py')

# Set up a tokens.py file if it does not already exist
def init_tokens_file():
	'''Initialize tokens file'''
	if not os.path.exists(TOKENS_FILE):
		import base64, uuid
		with open(TOKENS_FILE, 'w') as f:
			f.write('COOKIE_SECRET = "{}"\n'.format(base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)))
			f.write('FB_TOKEN = "OAuth token for Facebook"\n')
			f.write('TW_APP_KEY = "This and the next 3 are OAuths for Twitter"\n')
			f.write('TW_APP_SECRET = ""\n')
			f.write('TW_OAUTH_TOKEN = ""\n')
			f.write('TW_OAUTH_SECRET = ""\n')

def pass_gen():
	'''Generate user password'''
	import getpass
	import hashlib
	import imp
	tokens = imp.load_source('tokens', TOKENS_FILE)

	def sha(data):
		return hashlib.sha256(repr(data) + tokens.COOKIE_SECRET).hexdigest()

	# Convert to unicode since get_argument() in Tornado returns unicode!
	print sha(unicode(getpass.getpass()))

def install():
	'''Install Parrot'''
	with strap.virtualenv('tornado'):
		strap.run([
			'easy_install greenlet',
			'pip install motor',
			'pip install pattern',
			init_tokens_file
		]).freeze('requirements.txt')

def server():
	'''Start Parrot server'''
	with strap.virtualenv('tornado'):
		strap.run('python parrot')

def default():
	strap.run(server)
