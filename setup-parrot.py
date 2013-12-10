import os, sys, platform
from subprocess import call


DIRNAME = os.path.abspath(os.path.dirname(__file__))
ENV = 'tornado'
REQUIREMENTS = 'requirements.txt'


# Check if virtualenv is installed, and install if not
def check_virtualenv():
	print('== 1. Checking virtualenv ==')
	try:
		import virtualenv
	except ImportError:
		print('virtualenv not installed, installing now...')
		call('pip install virtualenv', shell=True)

# Check if our virtual environment is already created, and create if not
def check_env():
	print('== 2. Checking virtual environment ==')
	if not os.path.isdir(ENV):
		print('Creating virtual environment at {}...'.format(os.path.basename(ENV)))
		call('virtualenv {}'.format(ENV), shell=True)

# Install all necessary requirements to the virtual environment
def install_requirements():
	print('== 3. Installing requirements ==')
	script_dir = '\\Scripts\\' if platform.system() == 'Windows' else '/bin/'
	call('{}{}easy_install greenlet'.format(ENV, script_dir), shell=True)
	call('{}{}pip install motor'.format(ENV, script_dir), shell=True)
	call('{}{}pip freeze > {}'.format(ENV, script_dir, REQUIREMENTS), shell=True)


def main():
	# Make sure we work in directory next to current file
	os.chdir(DIRNAME)
	check_virtualenv()
	check_env()
	install_requirements()
	print('== Parrot Installation Complete! ==')


if __name__ == '__main__':
	main()