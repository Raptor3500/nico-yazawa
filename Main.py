# Nico Yazawa by AgentHi5

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import loadconfig
import os

startup_extensions = loadconfig.__cogs__
bot = commands.Bot (command_prefix='!')

bot.remove_command('help')

async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name='a guard suffer.', type=3)
        await bot.change_presence(game=discord.Game(name='Snake Eater.', type=2)   
        await bot.change_presence(game=discord.Game(name='super secret documents.', type=1, url='http://twitch.tv/hauntedshadowslegacy')

@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
                                  
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
