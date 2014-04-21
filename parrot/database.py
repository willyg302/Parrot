from tornado import gen, ioloop

import motor
from pymongo.errors import ConnectionFailure

import parrot_settings
from logger import log


class DB:

	def __init__(self):
		self.available = False
		try:
			client = motor.MotorClient()
			ioloop.IOLoop.current().run_sync(client.open)  # Test if MongoDB is up
			self._db = client[parrot_settings.DB_NAME]
			self.available = True
		except ConnectionFailure, e:
			log.error('Unable to connect to database {}!'.format(parrot_settings.DB_NAME))

	'''
	@gen.coroutine
	def bulk_insert(collection, generator):
		if not self.available:
			return
		yield self._db[collection].insert(generator)
	'''


	'''
	>>> @gen.coroutine
... def f():
...     yield db.test.insert(({'i': i} for i in xrange(10000)))
...     count = yield db.test.count()
...     print("Final count: %d" % count)
>>>
>>> IOLoop.current().run_sync(f)
Final count: 10000'''