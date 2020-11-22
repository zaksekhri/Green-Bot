"""
This file will mainly include general/uncategorized functions that I use here and there
"""

# Imports
import discord
from discord.ext import commands
import requests, json

#Functions
def is_owners():
    def predicate(ctx):
        return ctx.message.author.id in ctx.bot.credentials['bot']['owners']
    return commands.check(predicate)

def listToString(lis) -> str:
	# initialize empty string 
    str1 = ""  
    
    # traverse in the string   
    for item in lis:  
        str1 += item 
    
    # return string
    return str1

def listToSpacedString(lis) -> str:
    # initialize empty string 
    str1 = ""  
    
    # traverse in the string   
    for item in lis:  
        str1 += " " + item 
    
    # return string
    return str1

def infoListToString(lis) -> str:
    output = lis[0]
    
    for item in lis[1:]:
        output += f', {item}' 

    return output

async def convert_with_fallback(converter, datum, fallback_value):
    try:
        return await getattr(commands, converter)().convert(ctx=ctx, argument=datum)
    except Exception as e:
        print(e)
        return fallback_value

async def fetchAPI(apiURL):
    output = requests.get(apiURL).json()

    return output