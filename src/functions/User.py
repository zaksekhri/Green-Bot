# Imports
import discord
from discord.ext import commands

# Class
class User():
	"""docstring for User"""
	def __init__(self, user):
		super(User, self).__init__()
		self.base_user = user

	async def perm_check(self):
		"""
		member.guild_permissions.manage_roles
		https://discordpy.readthedocs.io/en/latest/api.html?highlight=permissions#discord.Permissions.create_instant_invite
		"""
		output = {
			"create_instant_invite": self.base_user.guild_permissions.create_instant_invite,
			"kick_members": self.base_user.guild_permissions.kick_members,
			"ban_members": self.base_user.guild_permissions.ban_members,
			"manage_channels": self.base_user.guild_permissions.manage_channels,
			"administrator": self.base_user.guild_permissions.administrator,
			"manage_guild": self.base_user.guild_permissions.manage_guild,
			"add_reactions": self.base_user.guild_permissions.add_reactions,
			"view_audit_log": self.base_user.guild_permissions.view_audit_log,
			"priority_speaker": self.base_user.guild_permissions.priority_speaker,
			"stream": self.base_user.guild_permissions.stream,
			"read_messages": self.base_user.guild_permissions.read_messages,
			"view_channel": self.base_user.guild_permissions.view_channel,
			"send_messages": self.base_user.guild_permissions.send_messages,
			"send_tts_messages": self.base_user.guild_permissions.send_tts_messages,
			"manage_messages": self.base_user.guild_permissions.manage_messages,
			"embed_links": self.base_user.guild_permissions.embed_links,
			"attach_files":self.base_user.guild_permissions.attach_files,
			"read_message_history": self.base_user.guild_permissions.read_message_history,
			"mention_everyone": self.base_user.guild_permissions.mention_everyone,
			"external_emojis": self.base_user.guild_permissions.external_emojis,
			"use_external_emojis": self.base_user.guild_permissions.use_external_emojis,
			"view_guild_insights": self.base_user.guild_permissions.view_guild_insights,
			"connect": self.base_user.guild_permissions.connect,
			"speak": self.base_user.guild_permissions.speak,
			"mute_members": self.base_user.guild_permissions.mute_members,
			"deafen_members": self.base_user.guild_permissions.deafen_members,
			"move_members": self.base_user.guild_permissions.move_members,
			"use_voice_activation": self.base_user.guild_permissions.use_voice_activation,
			"change_nickname": self.base_user.guild_permissions.change_nickname,
			"manage_nicknames": self.base_user.guild_permissions.manage_nicknames,
			"manage_roles": self.base_user.guild_permissions.manage_roles,
			"manage_permissions": self.base_user.guild_permissions.manage_permissions,
			"manage_webhooks": self.base_user.guild_permissions.manage_webhooks,
			"manage_emojis": self.base_user.guild_permissions.manage_emojis
		}

		return output
