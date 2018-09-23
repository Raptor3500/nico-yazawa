import discord
from discord.ext import commands

OK = 0x89f442
Error = 0xf44141

class Help():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', aliases=["Help"])
    async def _help(self):
        embed = discord.Embed(
            name='Help',
            color=0xffd700
        )
        embed.add_field(name='about [info]', value="This command is not finished.", inline=False)
        embed.add_field(name='commands [cmds]', value='This command is not finished.', inline=False)
        embed.add_field(name='modules [cogs]', value='This command is not finished.', inline=False)
        await self.bot.say(embed=embed)

    @commands.command(name='modules', aliases=['Modules', 'cogs', 'Cogs'])
    async def _modules(self):
        embed = discord.Embed(name=None, color=OK)
        embed.add_field(name='List of modules', value='Owner\nHelp', inline=False)
        await self.bot.say(embed=embed)

    @commands.command(name='cmds', aliases=['Cmds', 'commands', 'Commands'])
    async def _cmds(self, str : str):
        str = str.strip()
        embed = discord.Embed(name=str, description=description, color=OK)
        if 'Owner' or 'owner' in str:
            str = 'Owner'
            description = 'These commands are [Owner Only] commands.'

    @commands.command(name='about', aliases=['About', 'info', 'Info'])
    async def _about(self):
        embed = discord.Embed(name=None, color=OK)
        embed.add_field(name='v1.1-dev', value='About Me!', inline=False)
        embed.add_field(name='Nico Yazawa Developer', value='AgentHi5#5584', inline=False)
        embed.add_field(name='GitHub', value='AgentHi5/nico-yazawa', inline=False)
        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
