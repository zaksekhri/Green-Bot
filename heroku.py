import discord
from discord.ext import commands
import sys, os, traceback, json, logging, time, platform, requests
import datetime as dt
from datetime import datetime
from src.functions.embedC import embedC


def credentials():
    with open('heroku_info.json') as credentials:
        data = json.load(credentials)
    return data

def prefix(bot, message):
    bot.commands_run += 1
    return commands.when_mentioned_or(credentials()['bot']['defprefix'])(bot, message)
    
intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(
    command_prefix=prefix,
    owner_id=credentials()['bot']['owners'][0],
    intents=intents
    )

# Global Attributes
setattr(bot, "credentials", credentials())
# setattr(bot, "logger", logger)
bot.starttime = time.monotonic()
bot.commands_run = 0

for cog in bot.credentials['bot']['cogs']:
    try:
        bot.load_extension(f'src.extensions.{cog}')
        print(f"Successfully loaded {cog}")
    except Exception as e:
        print(f'Failed to load cog {cog}. --', file=sys.stderr)
        traceback.print_exc()

# bot.add_check(lambda ctx: ctx.guild)

# This checks if a command was run in a server or not, if not it checks the author ID and if it's not an owners ID it passes
@bot.check
async def inguild(ctx):
    if ctx.author.id in bot.credentials['bot']['owners']:
        return True
    return ctx.guild

@bot.command()
async def info(ctx):
    total_seconds = time.monotonic() - bot.starttime
    mins, secs = divmod(total_seconds, 60)
    hours, mins = divmod(mins, 60)
    uptime = f"{int(hours)} Hours {int(mins)} Minutes {int(secs)} Seconds"

    # convert to cardinal
    description = requests.get('https://raw.githubusercontent.com/zaksekhri/Green-Bot/master/data/botinfo.txt').text
    description = description.format(
        platform.python_version(), discord.__version__, bot.credentials['version'], uptime, len(ctx.bot.guilds), len(ctx.bot.users), bot.commands_run
    )
    embed = embedC.quick_embed("General Information", description, 0x363940)
    embed.set_thumbnail(url=ctx.me.avatar_url_as(size=256))

    await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def kys(ctx):
    await ctx.send("Bot is shutting down.")
    print("\nBot has shut down.")

    await bot.close()
    
@bot.command()
async def ping(ctx):
    latency = bot.latency
    print(f"Latency: {latency}")
    await ctx.send(f"Pong! Latency: {latency}")

@bot.event
async def on_ready():

    print(f'\nLogged in as: {bot.user.name} - {bot.user.id}\nDiscord.py Version: {discord.__version__}\n')
    
    init_status = discord.Status.online
    init_game = discord.Game(name='the role of a test subject.')
    await bot.change_presence(status=init_status, activity=init_game)

    print(f'Successfully logged in and booted...!')

bot.run(os.getenv('TOKEN'), bot=True)