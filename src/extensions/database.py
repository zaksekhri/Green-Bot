# Imports
import discord
from discord.ext import commands

# Class
class DatabaseCog(commands.Cog):
	"""docstring for database"""
	def __init__(self, bot):
		super(database, self).__init__()
		self.dbconn = psycopg2.connect("dbname=suppliers user=postgres password=postgres")
		
def setup(bot):
    bot.add_cog(DatabaseCog(bot))