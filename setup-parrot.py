import os, platform, importlib
from subprocess import call


DIRNAME = os.path.abspath(os.path.dirname(__file__))
ENV = 'tornado'
REQUIREMENTS = 'requirements.txt'
TOKENS_FILE = 'tokens.py'

script_dir = '\\Scripts\\' if platform.system() == 'Windows' else '/bin/'


# Checks to see if [package] is installed, and if not calls [command] to install it
def bootstrap_package(package, command):
	print('Checking whether {} is installed...'.format(package))
	try:
		importlib.import_module(package)
	except ImportError:
		print('{} not installed, installing now...'.format(package))
		call(command, shell=True)

# Invokes a shell command relative to our virtual environment
def call_virtual(command):
	call('{}{}{}'.format(ENV, script_dir, command), shell=True)


# Check for and installs dependencies
def check_dependencies():
	print('== 1. Checking dependencies ==')
	bootstrap_package('setuptools', 'python setup/ez_setup.py')
	bootstrap_package('pip', 'python setup/get-pip.py')
	bootstrap_package('virtualenv', 'pip install virtualenv')

# Check if our virtual environment is already created, and create if not
def check_env():
	print('== 2. Checking virtual environment ==')
	if not os.path.isdir(ENV):
		print('Creating virtual environment at {}...'.format(os.path.basename(ENV)))
		call('virtualenv {}'.format(ENV), shell=True)

# Install all necessary requirements to the virtual environment
def install_requirements():
	print('== 3. Installing requirements ==')
	call_virtual('easy_install greenlet')
	call_virtual('pip install motor')
	call_virtual('pip install pattern')
	call_virtual('pip freeze > {}'.format(REQUIREMENTS))

# Set up a tokens.py file if it does not already exist
def init_tokens_file():
	print('== 4. Initializing {} =='.format(TOKENS_FILE))
	if not os.path.exists(TOKENS_FILE):
		import base64, uuid
		with open(TOKENS_FILE, 'w') as f:
			f.write('COOKIE_SECRET = "{}"\n'.format(base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)))
			f.write('FB_TOKEN = "OAuth token for Facebook"\n')
			f.write('TW_APP_KEY = "This and the next 3 are OAuths for Twitter"\n')
			f.write('TW_APP_SECRET = ""\n')
			f.write('TW_OAUTH_TOKEN = ""\n')
			f.write('TW_OAUTH_SECRET = ""\n')


def main():
	os.chdir(DIRNAME)  # Make sure we work in directory next to current file
	check_dependencies()
	check_env()
	install_requirements()
	init_tokens_file()
	print('== Parrot Installation Complete! ==')


if __name__ == '__main__':
	main()