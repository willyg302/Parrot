Parrot
======

A social media data collection framework.

Setup
-----

> **Note**: All instructions below, unless otherwise stated, assume a UNIX environment. Depending on your privileges you may need to `sudo` things or be logged in as an administrator on Windows. You should also be in the Parrot/ directory to start off.

1. Get [Python](http://www.python.org/) (we use various versions of 2.7)

2. Install `setuptools` and `pip` for your Python environment (if you have these already, you can skip this step)

   ```bash
   $ python setup/ez_setup.py
   $ python setup/get-pip.py
   ```

3. Create a virtual environment for Parrot

   ```bash
   $ pip install virtualenv
   $ virtualenv tornado
   ```

4. Install the necessary packages

   ```bash
   $ tornado/bin/pip install -r requirements.txt
   ```

   Or on Windows:

   ```bash
   $ tornado\Scripts\pip install -r requirements.txt
   ```

And that's it! ...Okay not really. The next step is to set up proper authorization for Parrot (OAuth, secret keys, cookies, and all that good stuff).

Authorization
-------------

### Setting up tokens.py

Make a file in the root directory Parrot/ called `tokens.py`. This file has the following format:

```python
COOKIE_SECRET = 'my super secret cookie key thing here'
FB_TOKEN = 'OAuth token for Facebook'
TW_APP_KEY = 'This and the next 3 are OAuths for Twitter'
TW_APP_SECRET = ''
TW_OAUTH_TOKEN = ''
TW_OAUTH_SECRET = ''
```

You can generate a `COOKIE_SECRET` very easily by using the following Python script:

```python
import base64
import uuid
base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
```

To get the remaining **OAuth tokens** for the various social media sites, you will need to set up apps and developer accounts with them. This is left as an exercise for the reader.

**Warning**: If you do not include this file, Parrot will not run. You may choose to omit certain tokens if you do not need them, but you must at least include the `COOKIE_SECRET`.

### Defining users

By default, Parrot is password-protected by a login page. This is to prevent random people from using up the data collection quotas.

Parrot defines a set of known users as a Python dictionary called `USER_DICT` in `parrot_settings.py`. The key is the username, and the value is a salted sha256 of the corresponding password. There are a few users defined already but they probably won't be of much use to you, so delete them all.

You can create a new user by simply adding them to the dictionary. To get the password, run `python pass_gen.py` and enter a password at the prompt. The program will spit out the salted pass that you can then put into `USER_DICT`.

Usage
-----

Execute `run.bat` on Windows or `sh run.sh` on UNIX to start the server.

Credits
-------

* __Python for Facebook__: [Facebook Python SDK](https://github.com/pythonforfacebook/facebook-sdk)
* __Ryan McGrath__: [Twython](https://github.com/ryanmcgrath/twython)