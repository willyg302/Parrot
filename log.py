import os
import sys
import logging
from parrot_settings import LOG_PATH

if not os.path.exists(LOG_PATH):
	os.makedirs(LOG_PATH)

LOG_FILE_NAME = os.path.join(LOG_PATH, 'parrot.log')

parrot_log = logging.getLogger('parrot')
std_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('{}'.format(LOG_FILE_NAME))
formatter = logging.Formatter('[%(levelname)s %(module)s %(asctime)s] %(message)s')
std_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
parrot_log.addHandler(std_handler)
parrot_log.addHandler(file_handler)