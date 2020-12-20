# Imports
import datetime as dt
from datetime import datetime
import operator
import discord
from discord.ext import commands
from ..functions.embedC import embedC
from ..functions.general import fetchAPI
from ..functions.date import Date
from ..functions.menu import menuManager

# CLass
class WarframeCog(commands.Cog):
	"""docstring for WarframeCog"""
	def __init__(self, bot):
		super(WarframeCog, self).__init__()
		self.bot = bot

	base_api = "https://api.warframestat.us/pc"
	api_extentions = {
		"cetus": "/cetusCycle",
		"vallis": "/vallisCycle",
		"cambion": "/cambionCycle",
		"arbi": "/arbitration",
		"kuva": "/kuva",
		"sortie": "/sortie",
		"fissures": "/fissures",
		"invasions": "/invasions",
		"events": "/events"
	}
	relic_tiers = ["Lith", "Meso", "Neo", "Axi", "Requiem"]

	async def fetchWFAPI(self, extention = None):
		url = self.base_api 
		if extention is not None:
			url += self.api_extentions[extention]

		warframe_api = await fetchAPI(url)

		return warframe_api

	@commands.command(name="server-index", aliases=['server-list'])
	async def server_index(self, ctx):
		embed = embedC.quick_embed(f"Server Index", None, 0x98FB98)

		fields = [
			{"name": "General Warframe Servers", "value": "\
			[Official Warframe Server](https://discord.gg/cV6KV3G)\
			\n[Community Warframe Server](https://discord.gg/warframe)\
			\n[Warframe Trading Hub](https://discord.gg/EwD6J37)\
			\n[Warframe Blessings](https://discord.gg/3hHy5ygR4y)\
			\n[Warframe Giveaways](https://discord.com/invite/d8ZYADy)\
			\n[Endgame Community](https://discord.gg/2REYJrK)", "inline": True},
			{"name": "Topical Warframe Servers", "value": "\
			[Warframe University](https://discord.gg/ftfPKjP)\
			\n[Warframe Speedruns](https://discord.gg/7wtcKvv)\
			\n[Riven Info and Trading](https://discord.gg/S7aCrWx)\
			\n[Eidolon Zone](https://discord.gg/jDkrGf7)\
			\n[Warframe Arbitrations](https://discord.gg/ENRWGZr)\
			\n[Warframe Railjack](https://discord.gg/JvYVMNa)\
			\n[Warframe Conclave](https://discord.gg/asJsw6Q)\
			\n[Kubrow & Kavat Breeding and Trading](https://discord.gg/abzV2Cb)", "inline": True}
		]

		embedC().builder(embed, ctx.author, fields)

		await ctx.send(embed=embed)

	@commands.command(name="free-glyphs")
	async def free_glyphs(self, ctx):
		await ctx.send("<https://levvvel.com/warframe-promo-codes/>")

	@commands.command(name="lich-spawning")
	async def lich_spawning(self, ctx):
		await ctx.send("https://media.discordapp.net/attachments/700538916239048794/706874824131346462/lich_weapons.JPG")

	@commands.command(name="amp-tiers")
	async def amp_tiers(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/723102443113807932/740248780842205224/AmpConvention.pnghttps://idalon.com/tools/analyzer")

	@commands.command(name="propa-game")
	async def propa_game(self, ctx):
		await ctx.send("https://idalon.com/games/propa")

	@commands.command(name="raplak-game")
	async def raplak_game(self, ctx):
		await ctx.send("https://idalon.com/games/raplak")

	@commands.command(name="hunt-analyzer")
	async def hunt_analyzer(self, ctx):
		await ctx.send("https://idalon.com/tools/analyzer")

	@commands.command(aliases=["arbi"],brief="Returns the current arbi info.")
	async def arbitration(self, ctx):
		info = await self.fetchWFAPI("arbi")

		embed = embedC.quick_embed("Current Arbitration", None, 0x98FB98)

		fields = [
			{"name" : "Enemy", "value" : info["enemy"], "inline" : True},
			{"name" : "Mission", "value" : info["type"], "inline" : True},
			{"name" : "Node", "value" : info["node"], "inline" : False}
		]

		if info["archwing"]:
			fields.append({"name": "Archwing", "value": info["archwing"], "inline": False})

		embedC().add_fields(embed, fields)

		embed.set_footer(text="Expiry", icon_url=ctx.author.avatar_url_as(size=256))
		embed.timestamp = datetime.strptime(info["expiry"],"%Y-%m-%dT%H:%M:%S.%fZ")

		await ctx.send(content=None,embed=embed)

	@commands.command(brief="Returns the current sortie info.")
	async def sortie(self, ctx):
		info = await self.fetchWFAPI("sortie")

		embed = embedC.quick_embed("Current Sortie", None, 0x98FB98)

		fields = [
			# {"name" : "Boss", "value" : f'{sortie_info["boss"]}\
			# \nFaction - {sortie_info["faction"]}', "inline" : "False"},
			{"name" : f'Mission One - {info["variants"][0]["missionType"]}', "value" : f'Node: {info["variants"][0]["node"]}\
			\n{info["variants"][0]["modifier"]}\
			\n - {info["variants"][0]["modifierDescription"]}', "inline" : False},
			{"name" : f'Mission Two - {info["variants"][1]["missionType"]}', "value" : f'Node: {info["variants"][1]["node"]}\
			\n{info["variants"][1]["modifier"]}\
			\n - {info["variants"][1]["modifierDescription"]}', "inline" : False},
			{"name" : f'Mission Three - {info["variants"][2]["missionType"]}', "value" : f'Node: {info["variants"][2]["node"]}\
			\n{info["variants"][2]["modifier"]}\
			\n - {info["variants"][2]["modifierDescription"]}', "inline" : False},
		]

		embedC().add_fields(embed, fields)

		embed.set_footer(text="Expiry", icon_url=ctx.author.avatar_url_as(size=256))
		embed.timestamp = datetime.strptime(info["expiry"],"%Y-%m-%dT%H:%M:%S.%fZ")

		await ctx.send(content=None, embed=embed)

	@commands.command(brief="Returns the current fissures.")
	async def fissures(self, ctx, tier = None):
		"""
		Convert to use paginator
		"""
		info = await self.fetchWFAPI("fissures")
		fields = []

		if tier != None:
			if tier.capitalize() in self.relic_tiers:
				tier = tier.capitalize()
				embed = embedC.quick_embed(f"Current {tier} Fissures", None, 0x98FB98)

				for fissure in info:
					if fissure["tier"] == tier:
						fields.append({"name": f'Mission Type: {fissure["missionType"]}', 
										"value" : f'Node: {fissure["node"]}\
											\nEnemy: {fissure["enemy"]}\
											\nExpires in: **{fissure["eta"]}**', "inline" : False})

				embedC().builder(embed, ctx.author, fields)
		
				await ctx.send(content=None, embed=embed)
			else:
				await ctx.send(f"**{tier}** is not a relic type!")
		else:
			pages = []

			lis = {"Lith" : "", "Meso" : "", "Neo" : "", "Axi" : "", "Requiem" : ""}

			for fissure in info:
				lis[fissure["tier"]] += (f'**Mission Type: {fissure["missionType"]}**\
											\nNode: {fissure["node"]} - Enemy: {fissure["enemy"]}\
											\nExpires in: {fissure["eta"]}\n')
			
			for relic, value in lis.items():
				if value != "":
					embed = embedC.quick_embed(f"{relic} Fissures", None, 0x98FB98)
					embed.description = value

					fields = []
					embedC().builder(embed, ctx.author, fields)

					pages.append(embed)

			m = menuManager(pages, "embed")
			await m.start(ctx)

	@commands.command(brief="Incomplete | Returns the current invasions.")
	async def invasions(self, ctx):
		info = await self.fetchWFAPI("invasions")
		pages = []

		"""			
		defender": "reward": {  "countedItems == count / type
		activation": "2020-12-13T13:40:01.458Z
		"attacker": "reward": {  "countedItems == count / type
		"""

		for invasion in info:
			if invasion["completed"] is True:
				embed = embedC.quick_embed(f'{invasion["desc"]} on {invasion["node"]}', None, 0x98FB98)

				fields = [
					{"name" : "Attacking Faction" , "value" : f'{invasion["attackingFaction"]}', "inline" : True},
					{"name" : "Defending Faction" , "value" : f'{invasion["defendingFaction"]}', "inline" : True},
					{"name" : "Active" , "value" : f'{invasion["completed"]}', "inline" : False},
					{"name" : "Rewards" , "value" : f'NA', "inline" : True}
				]
				
				embedC().builder(embed, ctx.author, fields)
				pages.append(embed)

		m = menuManager(pages, "embed")
		await m.start(ctx)

def setup(bot):
	bot.add_cog(WarframeCog(bot))
