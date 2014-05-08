import os

TOKENS_FILE = os.path.join('parrot', 'tokens.py')

# Set up a tokens.py file if it does not already exist
def init_tokens_file():
	if not os.path.exists(TOKENS_FILE):
		import base64, uuid
		with open(TOKENS_FILE, 'w') as f:
			f.write('COOKIE_SECRET = "{}"\n'.format(base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)))
			f.write('FB_TOKEN = "OAuth token for Facebook"\n')
			f.write('TW_APP_KEY = "This and the next 3 are OAuths for Twitter"\n')
			f.write('TW_APP_SECRET = ""\n')
			f.write('TW_OAUTH_TOKEN = ""\n')
			f.write('TW_OAUTH_SECRET = ""\n')

config = {
	'project': 'Parrot',
	'tasks': {
		'install': {
			'name': 'Install Parrot',
			'virtualenv': 'tornado',
			'run': [
				'easy_install greenlet',
				'pip install motor',
				'pip install pattern',
				init_tokens_file
			],
			'freeze': 'requirements.txt'
		},
		'default': {
			'run': ['install']
		}
	}
}