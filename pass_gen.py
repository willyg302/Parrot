import hashlib
import tokens

def sha(data):
	return hashlib.sha256(repr(data) + tokens.COOKIE_SECRET).hexdigest()

# Sanity check: remember get_argument() in Tornado always returns UNICODE!!!
# So we need to convert dem strings to unicode first
while True:
	password = raw_input('Enter a password: ')
	if password == '':
		break
	print sha(unicode(password))