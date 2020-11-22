# Imports
import discord
from discord.ext import commands
# Class
class UtilityCog(commands.cog):
	"""docstring for UtilityCog"""
	def __init__(self, bot):
		super(UtilityCog, self).__init__()
		self.bot = bot

def setup(bot):
    bot.add_cog(UtilityCog(bot))