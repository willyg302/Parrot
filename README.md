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

Collecting data from the various social media sites requires authorization in the form of __OAuth tokens__. Parrot specifies the required tokens in a file called `tokens.txt` in the application root directory. This file has the following format:

```json
{
	"fb_token": "[FACEBOOK TOKEN HERE]"
}
```

If you do not include this file, Parrot will not run.

Credits
-------

* __Python for Facebook__: [Facebook Python SDK](https://github.com/pythonforfacebook/facebook-sdk)
* __Ryan McGrath__: [Twython](https://github.com/ryanmcgrath/twython)