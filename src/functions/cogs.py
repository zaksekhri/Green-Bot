#Imports
import discord

# Loads cogs based on the passed name
async def loadCog(bot, cog):
	msg = ''

	try:
		bot.load_extension(f"src.extensions.{cog}")
	except Exception as e:
		msg = f'**`ERROR:`** {type(e).__name__} - {e}'
	else:
		msg = f'Successfully loaded src.extensions.{cog}'

	print(msg)
	return msg

async def unloadCog(bot, cog):
	msg = ''

	try:
		bot.unload_extension(f"src.extensions.{cog}")
	except Exception as e:
		msg = f'**`ERROR:`** {type(e).__name__} - {e}'
	else:
		msg = f'Successfully unloaded src.extensions.{cog}'

	print(msg)
	return msg

async def reloadCog(bot, cog):
	msg = ''

	try:
		bot.unload_extension(f"src.extensions.{cog}")
		bot.load_extension(f"src.extensions.{cog}")
	except Exception as e:
		msg = f'**`ERROR:`** {type(e).__name__} - {e}'
	else:
		msg = f'Successfully reloaded src.extensions.{cog}'

	print(msg)
	return msg