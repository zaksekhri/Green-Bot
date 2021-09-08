"""
Cardinal is my internal utility and management class to aid with bot development
"""

# Imports
from .general import is_owners
from .cogs import loadCog, unloadCog, reloadCog
from .Cardinal.logger_config import logC

# Class
class cardinal:
	"""docstring for cardinal"""
	def __init__(self):
		super(cardinal, self).__init__()

	# Global is Owner Check
	is_owners = is_owners()

	def logC(self):
		logr = logM(self)
		return logr