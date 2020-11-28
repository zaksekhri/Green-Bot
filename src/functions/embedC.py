import discord
from discord.ext import commands
from .date import Date
# https://gist.github.com/HidekiHrk/7c00b9b6d70a571e0034ea2667f15c40

class embedC:
	"""docstring for embedC"""
	def __init__(self):
		super(embedC, self).__init__()

	EMPTY = "\uFEFF"

	@staticmethod
	def quick_embed(title, desc, color):
		embed = discord.Embed(title=title, description=desc, colour=color, timestamp=Date.utcnow)

		return embed

	@staticmethod
	def add_fields(embed, fields):
		for field in fields:
			embed.add_field(name=field["name"], value=field["value"], inline=field["inline"])

	def builder(self, embed, author, fields, *, thumbnail = None):
		# make author a keyword arg like thumbnail as now it seems redundant to have it mandatory
		embed.set_footer(text=f'Info called by {author.name}#{author.discriminator}', icon_url=author.avatar_url_as(size=256))

		if thumbnail:
			embed.set_thumbnail(url=str(thumbnail))

		self.add_fields(embed, fields)

	def insert_field_at(embed, index, field):
		embed.insert_field_at(index, name=field["name"], value=field["value"], inline=field["inline"])

	def swap_fields(self, embed, fields):
		embed.clear_fields()

		self.add_fields(embed, fields)