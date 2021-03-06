import discord
from discord.ext import commands

class noflippedtables():
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.author.bot: return
        if '(╯°□°）╯︵ ┻━┻' in message.content:
            await self.bot.send_message(message.channel, "┬─┬ ノ( ゜-゜ノ)")

def setup(bot):
    bot.add_cog(noflippedtables(bot))
