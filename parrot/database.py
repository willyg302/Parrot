import motor
from pymongo.errors import ConnectionFailure

import parrot_settings
from logger import log


class DB:

	def __init__(self):
		self.available = False
		try:
			client = motor.MotorClient().open_sync()
			self._db = client[parrot_settings.DB_NAME]
			self.available = True
		except ConnectionFailure, e:
			log.error('Unable to connect to database {}!'.format(parrot_settings.DB_NAME))