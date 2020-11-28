import requests

def credentials():
    with open('heroku_info.json') as credentials:
        data = json.load(credentials)
    return data




"""
description = description.format(
    platform.python_version(), discord.__version__, bot.credentials['version'], uptime, len(ctx.bot.guilds), len(ctx.bot.users), bot.commands_run
)
"""
print(description)
print(desc)