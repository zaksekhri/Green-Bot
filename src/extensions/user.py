# Import
import discord
from discord.ext import commands
from ..functions.date import Date
from ..functions.embeds import embedC
from ..functions.general import listToSpacedString

# Class
class UserCog(commands.Cog):
	"""docstring for UserCog"""
	def __init__(self, bot):
		super(UserCog, self).__init__()
		self.bot = bot

	@commands.group(name="user", pass_context=True) # , invoke_without_command=False
	async def user(self, ctx):
		if ctx.invoked_subcommand is None:
			pass

	@user.command(name="info")
	async def user_info(self, ctx, *, member: discord.Member = None):
		if not member:
			member=ctx.author

		embed = embedC().quick_embed(f'User Info for {member.name}#{member.discriminator}', member.mention, 0x98FB98)
		joinInfo = f"{Date().quick_format(member.joined_at.date(),'long-date1')} \n {abs(Date().relative_time(member.joined_at,Date.now).days)} days ago"
		regInfo = f"{Date().quick_format(member.created_at.date(),'long-date1')} \n {abs(Date().relative_time(member.created_at,Date.now).days)} days ago"

		roles = ""
		rolecount = 0
		for role in member.roles[1:]:
			roles = (f"{role.mention} ") + roles
			rolecount += 1

		fields = [
			{"name" : 'User ID', "value" : member.id, "inline" : True},
			{"name" : "Nickname", "value" : member.nick, "inline" : True},
			{"name" : "Status", "value" : member.status, "inline" : True},
			{"name" : "Join Date", "value" : joinInfo, "inline" : True},
			{"name" : "Registered", "value" : regInfo, "inline" : True},
			{"name" : "Bot", "value" : member.bot, "inline" : True},
			{"name" : "Name Color", "value" : member.colour, "inline" : False},
			{"name" : f"Roles [{rolecount}]", "value" : roles or "Nothing aside from ``@everyone``", "inline" : False},
			{"name" : "User Perms", "value" : "Temp", "inline" : False}
		]

		embedC().builder(embed, ctx.author, fields, thumbnail = member.avatar_url_as(size=256))

		# embed.add_field(name="Profile Pic URL", value=member.avatar_url, inline=False)
		# Advanced Info -- Roles>
		#  embed.add_field(name="Animated Avatar", value=member.is_avatar_animated, inline=True)   -- Tried this and it spat out jargon, will need to clean it up and 
		#  embed.add_field(name="Highest Role", value=member.top_role, inline=True)

		await ctx.send(content=None, embed=embed)

	@user.command(name="permsin")
	async def permsin(self, ctx, *args):
		"""
		returns the perm value of a mentioned user or the author in a specified or current channel
		Usage: pre)user permsin <member> <channel>
		Notes:
		 - would like to clean up the try/except section
		"""
		member = None
		channel = None

		async def convert_with_fallback(converter, datum, fallback_value):
			try:
				return await getattr(commands, converter)().convert(ctx=ctx, argument=datum)
			except Exception as e:
				print(e)
				return fallback_value
		# tries to convert the second arg to a channel obj
		try:
			channel = await convert_with_fallback('TextChannelConverter', args[1], ctx.channel)
		except Exception as e:
			# if there is no second arg or the second arg is not a channel obj then tries this
			if len(args) > 0:
				# if there are args
				member = await convert_with_fallback('MemberConverter', args[0], ctx.author)
				channel = await convert_with_fallback('TextChannelConverter', args[0], ctx.channel)
			else:
				# if no args are passed
				member = ctx.author
				channel = ctx.channel
		else:
			# if it succeeds, carries on to try to convert the first obj to a member obj
			member = await convert_with_fallback('MemberConverter', args[0], ctx.author)

		embed = embedC.quick_embed(f"Perms for {member.name} in {channel.name}", embedC.EMPTY, 0x98FB98)
		embedC().builder(embed, ctx.author, [{"name":"Perms", "value":member.permissions_in(channel), "inline":False}], thumbnail = member.avatar_url_as(size=256))

		await ctx.send(content=None, embed=embed)

	@user.command(brief="Changes the passed user's nickname on the server.")
	async def nickname(self, ctx, *args):
		"""
		Usage: pre)user nickname <user> nickname

		need to add a check for both the user and the bot having perms to change username
		"""
		member = None
		nickname = None
		async def convert_with_fallback(converter, datum, fallback_value):
			try:
				return await getattr(commands, converter)().convert(ctx=ctx, argument=datum)
			except Exception as e:
				print(e)
				return fallback_value

		try:
			print("1")
			member = await convert_with_fallback('MemberConverter', args[0], ctx.author)
			nickname = listToSpacedString(args[1:])
		except Exception as e:
			print("2")
			member = ctx.author
			nickname = listToSpacedString(args)

		print("3")
		print(member.name)
		print(nickname)
		await member.edit(nick=str(nickname))
		print("4")
		await ctx.send("is done hommie")

def setup(bot):
	bot.add_cog(UserCog(bot))