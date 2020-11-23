# Imports
import discord
from discord.ext import menus
from discord.ext import commands

class menuManager(menus.Menu):
    def __init__(self, pages, forbm):
        super(menu, self).__init__()
        self.pages = pages
        self.current_page = 0
        self.form = form

    async def update(self, form):
        if form == "embed":
            embed = self.pages[self.current_page]
            await self.message.edit(embed=embed)
        if form == "plain":
            content = self.pages[self.current_page]
            await self.message.edit(content=content)

    async def send_initial_message(self, ctx, channel):
        if form == "embed":
            return await channel.send(embed=self.pages[self.current_page])
        if form == "plain":
            return await channel.send(content=self.pages[self.current_page])
        
    def _skip_when(self):
        return len(self.pages) < 3
    
    @menus.button("\U000023ee", skip_if=_skip_when)
    async def jump_to_first(self, payload):
        self.current_page = 0
        await self.update()

    @menus.button("\U000027a1")
    async def previous_page(self, payload):
        if self.current_page > 0:
            self.current_page -= 1
            await self.update()

    @menus.button("\U000023f9")
    async def stop_pages(self, payload):
        self.stop()

    @menus.button("\U000025b6")
    async def next_page(self, payload):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            await self.update()

    @menus.button("\U00002b05", skip_if=_skip_when)
    async def jump_to_last(self, payload):
        self.current_page = len(self.pages) - 1
        await self.update()