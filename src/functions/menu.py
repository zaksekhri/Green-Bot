# Imports
import discord
from discord.ext import menus
from discord.ext import commands

class menuManager(menus.Menu):
	"""docstring for menu"""
	def __init__(self, pages):
		super(menu, self).__init__()
		self.pages = pages
		self.current_page = 0

	async def handler(self, form):
		if form == "embed":
			await self.embedHandler()
		else:
			await self.contentHandler()

	async def embedHandler(self):
		pass

	async def contentHandler(self):
		pass
		
	async def send_initial_message(self, ctx, channel):
        return await channel.send(embed=self.pages[self.current_page])
    def _skip_when(self):
        return len(self.pages) < 3

    async def change(self):
        embed = self.pages[self.current_page]
        await self.message.edit(embed=embed)

	@menus.button("\U000023ee", skip_if=_skip_when)
    async def jump_to_first(self, payload):
        self.current_page = 0
        await self.change()

    @menus.button("\U000027a1")
    async def previous_page(self, payload):
        if self.current_page > 0:
            self.current_page -= 1
            await self.change()

    @menus.button("\U000023f9")
    async def stop_pages(self, payload):
        self.stop()

    @menus.button("\U000025b6")
    async def next_page(self, payload):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            await self.change()

    @menus.button("\U00002b05", skip_if=_skip_when)
    async def jump_to_last(self, payload):
        self.current_page = len(self.pages) - 1
        await self.change()