# Imports
import datetime as dt
from datetime import datetime
import pytz, time, dateutil

# Class
class Date:
	"""docstring for Date"""
	def __init__(self):
		super(Date, self).__init__()

	# Constants
	now = dt.datetime.now()
	utcnow = dt.datetime.utcnow()
	FORMAT = {
	  "24h-timestamp" : "%Y-%m-%d %H:%M:%S",
	  "12h-timestamp" : "%Y-%m-%d %I:%M:%S %p",
	  "short-date" : "%Y-%m-%d",
	  "long-date1" : "%B %d, %Y",
	  "long-date2" : "%d %B, %Y",
	  "short-time" : "%H:%M",
	  "long-time" : "%H:%M:%S",
	  "short-12time" : "%I:%M %p",
	  "long-12time" : "%I:%M:%S %p"
	}
	"""
	"%S" : ["s", "sec", "second"],
	"%M" : ["m","min","minute"],
	"%m" : "",
	"%B" : "",
	"%Y" : ["y","year"],
	"""
	BLEH = {
		"s" : "%S", #second
		"M" : "%M", #minute
		"m" : "%m", #month as a digit, 1-12 
		"sm" : "%b", #month shorthand 
		"lm" : "%B", #month longhand
		"y" : "%Y", #year
		"sd" : "%a", #day of the week, short
		"d" : "%A", #day of the week
		"dm" : "%d", #day of the month
		"dy" : "%j" #day of the year
	}

	def quick_format(self, date, form: str) -> str: 
		"""
		Formats the provided date object and returns a str
		"""
		output = date.strftime(self.FORMAT[form])

		return output

	def string_to_format(self, args):
		"""
		converts a string to a datetime format to use
		"""
		output = ""
		FORMAT = self.BLEH

		for item in args:
			if item in FORMAT.keys():
				output += f" {FORMAT[item]}"

		return output

	def format_date(self, date, args):
		"""
		Formats the passed date depending on the passed args
		"""
		output = date.strftime(self.string_to_format(args))

		return output

	@staticmethod
	def relative_time(date, compare):
		"""
		Does some math to figure out how far ahead or behind a date is relative to now
		"""
		output = date - compare

		return output

	def date_input(self):
		"""
		Converts inputed date to a datetime object
		"""
		pass

	# date cleaner --> removes shit like - or , or : or / from a date string