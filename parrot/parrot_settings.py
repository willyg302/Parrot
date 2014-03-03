import os

# Vars local to this class (style rule: start with underscore)
_dirname = os.path.dirname(__file__)

# Actual exposed settings (style rule: all caps)
DEBUG = True
STATIC_PATH = os.path.join(_dirname, '..', 'static')
TEMPLATE_PATH = os.path.join(_dirname, '..', 'templates')
LOG_PATH = os.path.join(_dirname, '..', 'logs')

MAX_WAIT_SECONDS_BEFORE_SHUTDOWN = 3

# Hard-coded dictionary of users, we won't have that many so this is okay
USER_DICT = dict(
	admin='4884ef6785bcac3c8bc17ee3b16bea2009009ed136bf82f3762acebfca4b5b3e',
)