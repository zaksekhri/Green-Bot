# Imports
import discord
from discord.ext import commands
import math, cmath, operator

# Class
class Math(commands.Cog):
	"""docstring for Math"""
	def __init__(self, bot):
		super(Math, self).__init__()
		self.bot = bot
	
	OP_FUNC = {
	 "add" : "+",
	 "subtract" : "- ",
	 "multiply" : "*",
	 "divide" : ["/", "\\"],
	 "exponent" : "^",
	 "sqr" : "√",
	 "open bracket" : ["(", "]"],
	 "close bracket" : [")","]"]
	}

	order = ["brackets", "exponent", ""]


def setup(bot):
    bot.add_cog(Math(bot))