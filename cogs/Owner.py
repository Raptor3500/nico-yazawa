import discord
from discord.ext import commands

OK = 0x89f442
Error = 0xf44141
ownerID = "228293630199070730"

class Owner():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def load(self, ctx, extension_name : str):
        """Loads an extension."""
        if ctx.message.author.id == ownerID:
            extension_name = extension_name.strip()
            if "cogs." not in extension_name:
                extension_name = "cogs." + extension_name
                try:
                    self.bot.load_extension(extension_name)
                except (AttributeError, ImportError) as e:
                    embedError = discord.Embed(title=None, description=None, color=Error)
                    embedError.add_field(name='Cog Error', value="```py\n{}: {}\n```".format(type(e).__name__, str(e)), inline=True)
                    await self.bot.say(embed=embedError)
                    return
                    embed = discord.Embed(title=None, description=None, color=OK)
                    embed.add_field(name=extension_name, value="Cog loaded.")
                    await self.bot.say(embed=embed)
        else:
            self.bot.say("You don't have the permissions to load {}.").format(extension_name)

    @commands.command(pass_context=True)
    async def unload(self, ctx, extension_name : str):
        """Unloads an extension."""
        if ctx.message.author.id == ownerID:
            extension_name = extension_name.strip()
            if "cogs." not in extension_name:
                extension_name = "cogs." + extension_name
                self.bot.unload_extension(extension_name)
                embed = discord.Embed(title=None, description=None, color=OK)
                embed.add_field(name=extension_name, value="Cog unloaded.")
                await self.bot.say(embed=embed)
        else:
            self.bot.say("You don't have the permission to unload {}.").format(extension_name)




def setup(bot):
    bot.add_cog(Owner(bot))
