import os

# Vars local to this class (style rule: start with underscore)
_dirname = os.path.dirname(__file__)

# Actual exposed settings (style rule: all caps)
DEBUG = True
STATIC_PATH = os.path.join(_dirname, 'static')
TEMPLATE_PATH = os.path.join(_dirname, 'templates')

MAX_WAIT_SECONDS_BEFORE_SHUTDOWN = 3

# Hard-coded dictionary of users, we won't have that many so this is okay
USER_DICT = dict(
	admin='ac4ba088bb3b2ec03086772161390082a6e528ef5ccdc065e691a8b823a71305',
)