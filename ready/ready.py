import discord
import loadconfig
import asyncio

class ready():
    def __init__(self, bot):
        self.bot = bot

    def status_task(self):
        while True:
            await self.bot.change_presence(game=discord.Game(name='a guard suffer.', type=3)
            await self.bot.change_presence(game=discord.Game(name='Snake Eater.', type=2)
            await self.bot.change_presence(game=discord.Game(name='super secret documents.', type=1, url='http://twitch.tv/hauntedshadowslegacy')
        
    async def on_ready(self):
        print ("------")
        print ("Hey, my name is " + self.bot.user.name + ".")
        print ("My ID is " + self.bot.user.id)
        print ("And I am coded with discord.py v" + discord.__version__)
        print (loadconfig.__git__)
        print ("------")
        bot.loop.create_task(status_task())
        


def setup(bot):
    bot.add_cog(ready(bot))
