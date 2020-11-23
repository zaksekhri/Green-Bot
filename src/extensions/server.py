# Imports
import discord
from discord.ext import commands
from ..functions.general import infoListToString, convert_with_fallback
from ..functions.date import Date
from ..functions.embeds import embedC
from ..functions.guild import Guild
from ..functions.menu import menuManager

class InfoCog(commands.Cog):
    def __init__(self, bot):
        super(InfoCog, self).__init__()
        self.bot = bot

    # Information and Stats
        # Server ----------------------------------------------------------------------------------------------------------------------------------
    @commands.group(name="server", pass_context=True) #, invoke_without_command=True
    async def server(self, ctx):
        if ctx.invoked_subcommand is None:
            pass

    @server.command(name="info")
    async def server_info(self, ctx):
        guild = Guild(ctx.guild)

        embed = embedC.quick_embed(f"Server info for {guild.base_guild.name}", None, 0x98FB98)

        fields = [
            {"name" : "Region", "value" : guild.base_guild.region, "inline": True},
            {"name" : "Guild ID", "value" : guild.base_guild.id, "inline": True},
            {"name" : "Owner", "value" : str(guild.base_guild.owner), "inline": True},
            {"name" : "Creation Date", "value" : guild.base_guild.created_at.date(), "inline": True},
            {"name" : "Member Count", "value" : guild.base_guild.member_count, "inline": True},
            {"name" : "Human & Bot Count", "value" : f"Humans: {guild.human_count} | Bots: {guild.bot_count}", "inline": True},
            {"name" : "Text Channel Count", "value" : guild.text_channel_count, "inline": True},
            {"name" : "Voice Channel Count", "value" : guild.voice_channel_count, "inline": True},
            {"name" : "Category Count", "value" : guild.category_count, "inline": True}
        ]

        embedC().builder(embed, ctx.author, fields, thumbnail = guild.base_guild.icon_url_as(size=256))

        await ctx.send(embed=embed)
    
    @server.command(name="detailedinfo", aliases=['dinfo'])
    async def s_dinfo(self, ctx):
        """
        Prep for the four pages 

        This will be converted to use the paginator system
        """
        # 
        guild = Guild(ctx.guild)

        page_one = embedC().quick_embed(f"Detailed server info for {guild.base_guild.name}", "**Page One.** \nBasic information about the server", 0x4E814E)
        page_two = embedC().quick_embed(f"Detailed server info for {guild.base_guild.name}", "**Page Two.** \nMember and Role information.", 0x4E814E)
        page_three = embedC().quick_embed(f"Detailed server info for {guild.base_guild.name}", "**Page Three.** \nServer channel information.", 0x4E814E)
        page_four = embedC().quick_embed(f"Detailed server info for {guild.base_guild.name}", "**Page Four.** \nMisc information about the server", 0x4E814E)

        page_one_fields = [
            {"name" : "Region", "value" : guild.base_guild.region, "inline": True},
            {"name" : "Guild ID", "value" : guild.base_guild.id, "inline": True},
            {"name" : "Owner", "value" : str(guild.base_guild.owner), "inline": True},
            {"name" : "Creation Date", "value" : guild.base_guild.created_at.date(), "inline": True}
        ]

        roles = ""
        for role in guild.base_guild.roles[1:]:
            roles = (f"\n{role.mention} -- Members: {guild.role_member_count(role)}") + roles 

        page_two_fields = [
            {"name" : f"Roles [{guild.role_count}]", "value" : roles or "None aside from ``@ everyone``", "inline" : False},
            {"name" : "Member Count", "value" : guild.base_guild.member_count, "inline": True, "inline" : False},
            {"name" : "Human Count", "value" : guild.human_count, "inline" : False},
            {"name" : f"Bot List [{guild.bot_count}]", "value" : infoListToString(guild.bot_members) or f"There are no bots in {guild.base_guild.name}!", "inline" : False}
        ]

        tchannels = ""
        vchannels = ""
        cchannels = ""

        for channel in guild.base_guild.text_channels:
            tchannels += f"Name: {channel.mention}\n"
        for channel in guild.base_guild.voice_channels:
            vchannels += f"Name: {channel.mention}\n"
        for category in guild.base_guild.categories:
            cchannels += f"Name: {category.name}\n"

        page_three_fields = [
            {"name" : "Text Channel Count + List", "value" : f"Count: {guild.text_channel_count}\n{tchannels}", "inline" : False},
            {"name" : "Voice Channel Count + List", "value" : f"Count: {guild.voice_channel_count}\n{vchannels}", "inline" : False},
            {"name" : "Channel Category Count + List", "value" : f"Count: {guild.category_count}\n{cchannels}", "inline" : False},
        ]

        emojis = ""
        for emoji in guild.base_guild.emojis:
            emojis = emojis + (f"**{emoji.name}:** <:{emoji.name}:{emoji.id}>\n")

        page_four_fields = [
            {"name" : "Custom Emojis", "value" : emojis or f"{guild.base_guild.name} has no custom emojis!", "inline" : False},
            {"name" : "Server Features", "value" : guild.base_guild.features or f"{guild.base_guild.name} has no features!<:cry:441942123047288832>", "inline" : False},
            {"name" : "Server Icon Url", "value" : guild.base_guild.icon_url or f"{guild.base_guild.name} has no icon!", "inline" : False},
            {"name" : "Verification Level", "value" : guild.base_guild.verification_level, "inline" : False},
        ]

        embedC().builder(page_one, ctx.author, page_one_fields, thumbnail=guild.base_guild.icon_url_as(size=256))
        embedC().builder(page_two, ctx.author, page_two_fields, thumbnail=guild.base_guild.icon_url_as(size=256))
        embedC().builder(page_three, ctx.author, page_three_fields, thumbnail=guild.base_guild.icon_url_as(size=256))
        embedC().builder(page_four, ctx.author, page_four_fields, thumbnail=guild.base_guild.icon_url_as(size=256))

        pages = [page_one, page_two, page_three, page_four]

        m = menuManager(pages, "embed")
        await m.start(ctx)
        #message = await ctx.send(embed=page_one)

    @server.command()
    async def roles(self, ctx):
        guild = Guild(ctx.guild)

        embed = embedC().quick_embed(f"Server Roles for {guild.base_guild.name}", None, 0x98FB98)

        fields = [{"name" : f"Roles [{guild.role_count}]", "value" : infoListToString(guild.roles_string[1:]) or "None aside from ``@ everyone``", "inline" : False}]

        embedC().builder(embed, ctx.author, fields)

        await ctx.send(content=None, embed=embed)

    @server.command(name="membercount")
    async def membercount(self, ctx):
        guild = Guild(ctx.guild)

        embed = embedC().quick_embed(f"Member Count for {guild.base_guild.name}", None, 0x98FB98)

        fields = [
            {"name" : "Total Count", "value" : guild.base_guild.member_count, "inline" : False},
            {"name" : "Humans", "value" : guild.human_count, "inline" : True},
            {"name" : "Bots", "value" : guild.bot_count, "inline" : True}
        ]

        print(fields)

        embedC().builder(embed, ctx.author, fields, thumbnail = ctx.author.avatar_url_as(size=256))

        await ctx.send(embed=embed)

    @server.command(name="channelinfo")
    async def channelinfo(self, ctx, channel: discord.TextChannel = None):
        if not channel:
            channel = ctx.channel

        embed = embedC.quick_embed(f"Channel Info for {channel.name}", embedC.EMPTY, 0x98FB98)

        fields = [
            {"name" : "Channel ID", "value" : channel.id, "inline" : True},
            {"name" : "Member Count", "value" : len(channel.members), "inline" : True},
            {"name" : "Position", "value" : channel.position, "inline" : True},
            {"name" : "Category ID", "value" : channel.category_id, "inline" : True},
            {"name" : "Channel Topic", "value" : channel.topic or "No channel topic", "inline" : False}
        ]
        #embed.add_field(name="NSFW", value=channel.is_nswf, inline=True)
        #embed.add_field(name="Category Name", value=channel.category.name or "No Category", inline=True)
        
        embedC().builder(embed, ctx.author, fields, thumbnail = ctx.author.avatar_url_as(size=256))

        await ctx.send(content=None, embed=embed)

    @commands.command()
    async def createrole(self, ctx, rolename):
        server = ctx.guild
        try:
            role = await server.create_role(name=rolename)
        except Exception as e:
            await ctx.send("I don't have the perms to make roles!<:cry:441942123047288832>")
        else:
            embed = discord.Embed(title=f"Role Successfully Created!", description=None, colour=0x98FB98)
            embed.add_field(name="Role Name", value=f"{role}")
            embed.add_field(name="Role ID", value=f"{role.id}")
            embed.set_footer(text=f'Command called by {ctx.author.name}#{ctx.author.discriminator} at {dt.datetime.now().date()}', icon_url=ctx.author.avatar_url_as(size=256))
            
            await ctx.send(embed=embed)

    @commands.command()
    async def deleterole(self, ctx, rolename):
        for role in ctx.guild.roles:
            if role.name == rolename:
                therole = role
        rolename = therole.name
        roleid = therole.id
        try:
            await therole.delete()
        except Exception as e:
            await ctx.send("I don't have the perms to delete roles!<:cry:441942123047288832>")
        else:
            embed = discord.Embed(title=f"Role Successfully Deleted!", description=None, colour=0x98FB98)
            embed.add_field(name="Role Name", value=f"{rolename}")
            embed.add_field(name="Role ID", value=f"{roleid}")
            embed.set_footer(text=f'Command called by {ctx.author.name}#{ctx.author.discriminator} at {dt.datetime.now().date()}', icon_url=ctx.author.avatar_url_as(size=256))
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(InfoCog(bot))