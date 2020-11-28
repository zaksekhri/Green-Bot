# Imports
import discord
from discord.ext import menus
from discord.ext import commands
    
class menuManager(menus.Menu):
    def __init__(self, pages, form):
        super(menuManager, self).__init__()
        self.pages = pages
        self.current_page = 0
        self.form = form

    async def update(self, payload):
        """
        Overwrites base menu update func to delete user reaction
        """
        if self._can_remove_reactions:
            if payload.event_type == 'REACTION_ADD':
                await self.bot.http.remove_reaction(
                    payload.channel_id, payload.message_id,
                    discord.Message._emoji_reaction(payload.emoji), payload.member.id
                )
            elif payload.event_type == 'REACTION_REMOVE':
                return
        await super().update(payload)

    async def change(self) -> None:
        """
        Updates the message with the selected page.
        """
        if self.form == "embed":
            embed = self.pages[self.current_page]
            await self.message.edit(embed=embed)
        if self.form == "plain":
            content = self.pages[self.current_page]
            await self.message.edit(content=content)

    async def send_initial_message(self, ctx: commands.Context, channel: discord.TextChannel) -> discord.Message:
        """
        Sends the initial message.
        """
        if self.form == "embed":
            return await channel.send(embed=self.pages[self.current_page])
        if self.form == "plain":
            return await channel.send(content=self.pages[self.current_page])
    
    @menus.button("⏮")
    async def jump_to_first(self, _) -> None:
        """
        Jumps to the first page.
        """
        self.current_page = 0
        await self.change()

    @menus.button("◀")
    async def previous_page(self, _) -> None:
        """
        Jumps back one page.
        """
        if self.current_page > 0:
            self.current_page -= 1
            await self.change()

    @menus.button("❎")
    async def stop_pages(self, _) -> None:
        """
        Closes the paginator
        """
        self.stop()

    @menus.button("▶")
    async def next_page(self, _) -> None:
        """
        Jumps forward one page.
        """
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            await self.change()

    @menus.button("⏭")
    async def jump_to_last(self, _) -> None:
        """
        Jumps to last page.
        """
        self.current_page = len(self.pages) - 1
        await self.change()
