# Imports
import discord
from discord.ext import commands
from ..functions.general import listToSpacedString, convert_with_fallback
from ..functions.date import Date
from ..functions.embeds import embedC
from ..functions.guild import Guild

# Class
class inviteManager(commands.Cog):
	"""All commands which deal with invites, relies on the invite functions"""
	def __init__(self, bot):
		self.bot = bot

	def polish(self):
		k = invitePolish(self)
		return k

	@commands.command(brief="Lists info about all invites in the server.")
	async def invites(self, ctx):
		server = ctx.guild

		for invite in await server.invites():
			await ctx.send(invite.max_age)

	@commands.command(brief='Returns general information about the given invite link.')
	async def check_inv(self, ctx, invite):
		# invite = await convert_with_fallback("InviteConverter", invite, "bleh")

		invite = await commands.InviteConverter().convert(ctx=ctx, argument=invite)

		embed = embedC.quick_embed("Invite Info", None, 0x98FB98)

		fields = [
			{"name" : "Inviter", "value" : invite.inviter, "inline": True},
			{"name" : "Server Name", "value" : invite.guild.name, "inline": True},
			{"name" : "max age", "value" : invite.max_age, "inline": False},
			{"name" : "created at", "value" : invite.created_at, "inline": False},
			{"name" : "member count", "value" : invite.approximate_member_count, "inline": False},
			{"name" : "channel invited to", "value" : invite.channel, "inline": False},
			{"name" : "revoked", "value" : invite.revoked, "inline": False},
			{"name" : "temporary", "value" : invite.temporary, "inline": False},
			{"name" : "uses", "value" : invite.uses, "inline": False},
			{"name" : "max uses", "value" : invite.max_uses, "inline": False}
		]

		embedC().builder(embed, ctx.author, fields, thumbnail = invite.guild.icon_url_as(size=256))

		await ctx.send(content=None, embed=embed)

	@commands.command(brief="Deletes an invite.")
	async def delete_inv(self, ctx):
		pass

	@commands.command(brief="Creates an invite.")
	async def create_inv(self, ctx, *args):
		# incomplete according to intended usage
		# need to catch for no perm to create invite, and if the user can make invites as well
		"""
		Use Case
		gp.create_inv 
		gp.create_inv this is a reason
		gp.create_inv #general 
		gp.create_inv #general this is a reason
		"""
		channel = None
		reason = None

		async def convert_with_fallback(converter, datum, fallback_value):
			try:
				return await getattr(commands, converter)().convert(ctx=ctx, argument=datum)
			except Exception as e:
				print(e)
				return fallback_value

		try:
			channel = await convert_with_fallback('TextChannelConverter', args[0], ctx.channel)
		except Exception as e:
			raise e
		else:
			if channel is not ctx.channel:
				if len(args) >= 1:
					reason = listToSpacedString(args) + f" | Created by {ctx.author.name}#{ctx.author.discriminator}"
				else:
					reason = f"Created by {ctx.author.name}#{ctx.author.discriminator}"
			else:
				if len(args) >= 1:
					reason = listToSpacedString(args) + f" | Created by {ctx.author.name}#{ctx.author.discriminator}"
				else:
					reason = f"Created by {ctx.author.name}#{ctx.author.discriminator}"	

		invite = await channel.create_invite(reason = reason)

		await ctx.send(f"Created invite\n```{invite.url} for {channel.name}```")

	@commands.command(brief="Creates a temporary invite.")
	async def create_temp_inv(self, ctx, *, reason = None):


		invite = ctx.channel.create_invite(reason = reason, temporary=True)

class invitePolish:
	"""docstring for inviteHandler"""
	def __init__(self, inviteManager):
		super(inviteHandler, self).__init__()
		self.inviteManager = inviteManager

	def clean(self, invite):
		pass

	def age_converter(self, age):
		""" Age is an int, representing the age of the invite in seconds"""

		if age != 0: # if age is 0 then there is no expiry 
			# if age isnt 0 then converts to this shit
			minute = age/60
			hour = minute/60
			day = hour/24

			output = {
				"minute" : minute,
				"hour" : hour,
				"day" : day
			}

			return output
		else:
			# returns null for no expiry
			return null

def setup(bot):
	bot.add_cog(inviteManager(bot))