# Nico Yazawa by AgentHi5

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import loadconfig
import os

startup_extensions = loadconfig.__cogs__
bot = commands.Bot ()

bot.remove_command('help')

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

# Now that this bot has a repository on GitHub, I have removed the config of this bot.
# The name of the file has to be "loadconfig.py" or else this bot won't launch.
bot.run(loadconfig.__token__)
