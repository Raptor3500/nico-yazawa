import discord
import loadconfig
import asyncio

class ready():
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print ("------")
        print ("Hey, my name is " + self.bot.user.name + ".")
        print ("My ID is " + self.bot.user.id)
        print ("And I am coded with discord.py v" + discord.__version__)
        print (loadconfig.__git__)
        print ("------")
        await self.bot.change_presence(game=discord.Game(name='v1.1-dev'))


def setup(bot):
    bot.add_cog(ready(bot))
