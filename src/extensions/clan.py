# Imports
import discord
from discord.ext import commands

class ClanCog(commands.Cog):
	def __init__(self, bot):
		super(ClanCog, self).__init__()
		self.bot = bot

	@commands.command(name="propa-game")
	async def propa_game(self, ctx):
		await ctx.send("https://idalon.com/games/propa")

	@commands.command(name="raplak-game")
	async def raplak_game(self, ctx):
		await ctx.send("https://idalon.com/games/raplak")

	@commands.command(name="hunt-analyzer")
	async def hunt_analyzer(self, ctx):
		await ctx.send("https://idalon.com/tools/analyzer")

	@commands.command(name="lich-spawning")
	async def lich_spawning(self, ctx):
		await ctx.send("https://media.discordapp.net/attachments/700538916239048794/706874824131346462/lich_weapons.JPG")

	@commands.command(name="amp-tiers")
	async def amp_tiers(self, ctx):
		await ctx.send("https://cdn.discordapp.com/attachments/723102443113807932/740248780842205224/AmpConvention.pnghttps://idalon.com/tools/analyzer")

	@commands.command(name="build-wisp")
	async def build_wisp(self, ctx):
		await ctx.send("**Wisp Build -- 6** <:forma:774052452902240307>\n**Config A:** *<https://overframe.gg/build/91761/wisp/wisp-slot-a-general-use/>*\n**Config B:** *<https://overframe.gg/build/91347/wisp/wisp-slot-b-farming-hunting/>*\n**Config C:** *<https://overframe.gg/build/91765/wisp/wisp-slot-c-co-primer/>*")

	@commands.command(name="free-glyphs")
	async def free_glyphs(self, ctx):
		await ctx.send("<https://levvvel.com/warframe-promo-codes/>")

def setup(bot):
	bot.add_cog(ClanCog(bot))