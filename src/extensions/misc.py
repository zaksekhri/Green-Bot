# Imports
import discord
from discord.ext import commands
import random
#from ..functions.general import listToString

def listToString(lis):
	# initialize empty string 
    str1 = ""  
    
    # traverse in the string   
    for item in lis:  
        str1 += " " + item 
    
    # return string
    return str1

# Class
class Misc(commands.Cog):
	"""docstring for Misc"""
	def __init__(self, bot):
		super(Misc, self).__init__()
		self.bot = bot
	
	@commands.command()
	async def say(self, ctx, *args):
		"""
		Sends the provided message to the current channel, or a mentioned channel

		Use: pre)say [channel] [message]
		"""

		# Attempts to convert to a text channel, if it fails then passes
		try:
			# if it converts successfully then sends the content to the passed channel
			channel = await commands.TextChannelConverter().convert(ctx=ctx, argument=args[0])
			await channel.send(listToString(args[1:]))
		except:
			# if no channel is found then sends the content to ctx.channel
			await ctx.send(listToString(args))

	@commands.command(aliases=['rps'], brief="Outputs either rock, paper or scissors chosen by rand.choice()")
	async def rockpaperscissors(self, ctx):
		options = ['rock', 'paper', 'scissors']
		result = random.choice(options)

		await ctx.send(f"Result: {result}")

	@commands.command(brief="Outputs either heads or tails chosen by rand.choice()")
	async def coinflip(self, ctx):
		sides = ['heads', 'tails']
		result = random.choice(sides)

		await ctx.send(f"Result: {result}")

	@commands.command(aliases=['binvite'])
	async def botinvite(self, ctx, botID = None):
		# Generates a bot invite
		output = None

		if not botID:
			output = botID
		else:
			output = ctx.me.id

		await ctx.send(f"<https://discordapp.com/oauth2/authorize?client_id={output}&scope=bot&permissions=8>")

def setup(bot):
    bot.add_cog(Misc(bot))