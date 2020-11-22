# Imports
import discord
from discord.ext import commands
from .general import convert_with_fallback

# Class
class User(object):
	"""docstring for User"""
	def __init__(self, user):
		super(User, self).__init__()
		self.base_user = user
	
