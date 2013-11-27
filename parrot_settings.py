import os

# Vars local to this class (style rule: start with underscore)
_dirname = os.path.dirname(__file__)

# Actual exposed settings (style rule: all caps)
DEBUG = True
STATIC_PATH = os.path.join(_dirname, 'static')
TEMPLATE_PATH = os.path.join(_dirname, 'templates')

# Hard-coded dictionary of users, we won't have that many so this is okay
USER_DICT = dict(
	admin='23f0e94a2f81812f393ad95225b905ed9e9ee1a0a18b3ceacbcb4144e726b8f2',
)