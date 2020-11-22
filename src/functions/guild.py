# Imports
import discord
from discord.ext import commands
from .general import convert_with_fallback

# Class
class Guild:
	"""Custom Guild Class"""
	def __init__(self, guild):
		super(Guild, self).__init__()
		self.base_guild = guild

		self.bot_count = len([m for m in guild.members if m.bot])
		self.human_count = guild.member_count - self.bot_count
		self.online_count = sum([1 for m in guild.members if m.status == discord.Status.online])
		self.idle_count = sum([1 for m in guild.members if m.status == discord.Status.idle])
		self.dnd_count = sum([1 for m in guild.members if m.status == discord.Status.dnd])
		self.offline_count = sum([1 for m in guild.members if m.status == discord.Status.offline])
		self.text_channel_count = sum([1 for m in guild.text_channels])
		self.voice_channel_count = sum([1 for m in guild.voice_channels])
		self.category_count = sum([1 for m in guild.categories])
		self.role_count = sum([1 for m in self.base_guild.roles])

	# find(lambda status: status is not discord.Status.offline, (member.web_status, member.mobile_status, member.desktop_status)) or discord.Status.offline
	
	# Prevents custom attributes from being added during an instance
	# doesnt work yet
	#__slots__ = ('delete_text_channels')

	@property
	def bot_members(self):
		prot = [m.mention for m in self.base_guild.members if m.bot]
		return prot

	@property
	def roles_string(self) -> list:
		# needs a better name
		prot = [m.mention for m in self.base_guild.roles]
		return prot

	def member_count_in_roles(self, roles):
		"""
		Returns a list with the member count in each role

		[[role object, member count (int)],...]
		"""
		output = []

		for role in roles:
			output.append([role,sum(1 for m in role.members)])

		return output

	@staticmethod
	def role_member_count(role):
		# returns the number of members in the passed role
		prot = sum([1 for m in role.members])
		return prot

	def delete_channel(self, datum, channel):
		pass

	"""
	def delete_text_channels(self, datum):
		channels = self.base_guild.text_channels
		if type(datum) is not list:
			if datum is not "all":
				await convert('TextChannelConverter', datum, ctx.author)

	def delete_voice_channels(self, datum):
		pass
		
	def delete_channels(self, datum):
		pass

	def create_role_by_name(self, name):
		pass

	def delete_role_by_name(self, name):
		pass
	"""