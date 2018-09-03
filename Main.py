# Nico Yazawa by AgentHi5

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import loadconfig

startup_extensions = loadconfig.__cogs__
bot = commands.Bot (command_prefix=loadconfig.__prefix__)

@bot.event
async def on_ready():
    print ("------")
    print ("Hey, my name is " + bot.user.name + ".")
    print ("My ID is " + bot.user.id)
    print ("And I am coded with discord.py v" + discord.__version__)
    print ("------")


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(loadconfig.__token__)
