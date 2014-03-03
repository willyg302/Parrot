import os
import logging

from tornado.options import options
from tornado.log import LogFormatter

import parrot_settings


log = logging.getLogger('tornado.general')


def initialize_logging():
	if not os.path.exists(parrot_settings.LOG_PATH):
		os.makedirs(parrot_settings.LOG_PATH)
	
	channel = logging.handlers.RotatingFileHandler(
		filename=os.path.join(parrot_settings.LOG_PATH, 'parrot.log'),
		maxBytes=options.log_file_max_size,
		backupCount=options.log_file_num_backups
	)
	channel.setFormatter(LogFormatter(color=False))
	log.addHandler(channel)