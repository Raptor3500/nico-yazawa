import discord
from discord.ext import commands
from discord.utils import get

OK = 0x89f442
Error = 0xf44141

class general():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def emoji(self):
        emoji = get(self.bot.get_all_emojis(), name='floatyura')
        await self.bot.say(emoji)

def setup(bot):
    bot.add_cog(general(bot))
