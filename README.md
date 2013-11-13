Parrot
======

A social media data collection framework.

Setup
-----

1. `cd` into the __setup__ directory

2. Run the following commands in your favorite shell:

   ```bash
   $ python ez_setup.py
   $ python get-pip.py
   $ pip install facebook-sdk
   $ pip install twython
   ```

   Obviously this requires Python (2.7 is used by this project). If you already have `pip` installed, you can skip the first two commands.

Authorization
-------------

Collecting data from the various social media sites requires authorization in the form of __OAuth tokens__. Parrot specifies the required tokens in a file called `tokens.json` in the application root directory. This file has the following format:

```json
{
	"debug": {
		"fb_token": "[FACEBOOK TOKEN FOR TESTING]",
		"tw_app_key": "[TWITTER APP KEY FOR TESTING]",
		"tw_app_secret": "[TWITTER APP SECRET FOR TESTING]",
		"tw_oauth_token": "[TWITTER CLIENT OAUTH TOKEN FOR TESTING]",
		"tw_oauth_secret": "[TWITTER CLIENT OAUTH SECRET FOR TESTING]"
	},
	"production": {
		"fb_token": "[FACEBOOK TOKEN FOR PRODUCTION]",
		"tw_app_key": "[TWITTER APP KEY FOR PRODUCTION]",
		"tw_app_secret": "[TWITTER APP SECRET FOR PRODUCTION]",
		"tw_oauth_token": "[TWITTER CLIENT OAUTH TOKEN FOR PRODUCTION]",
		"tw_oauth_secret": "[TWITTER CLIENT OAUTH SECRET FOR PRODUCTION]"
	}
}
```

If you do not include this file, Parrot will not run. You may choose to omit certain tokens if you do not need them, or even the entire `debug` block if you never plan to run Parrot in debug mode.

Usage (CLI)
-----------

* `python parrot.py` to run Parrot (with all defaults, production mode)
* `python parrot.py --debug` to run Parrot in debug mode (also accepts `-d` shortcode)
* `python parrot.py --help` for a list of command line options

Credits
-------

* __Python for Facebook__: [Facebook Python SDK](https://github.com/pythonforfacebook/facebook-sdk)
* __Ryan McGrath__: [Twython](https://github.com/ryanmcgrath/twython)