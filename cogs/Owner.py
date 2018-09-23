import discord
from discord.ext import commands
import loadconfig

OK = 0x89f442
Error = 0xf44141
ownerID = loadconfig.ownerID

class Owner():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def load(self, ctx, extension_name : str):
        """Loads an extension."""
        extension_name = extension_name.strip()
        if "cogs." not in extension_name:
            extension_name = "cogs." + extension_name # nico load Owner => nico load cogs.Owner
            if ctx.message.author.id in ownerID:
                try:
                    self.bot.load_extension(extension_name)
                    embed = discord.Embed(title=None, description=None, color=OK)
                    embed.add_field(name=extension_name, value="Cog loaded.")
                    await self.bot.say(embed=embed)
                except (AttributeError, ImportError) as e:
                    embedError = discord.Embed(title=None, description=None, color=Error)
                    embedError.add_field(name='Cog Error', value="```py\n{}: {}\n```".format(type(e).__name__, str(e)), inline=True)
                    await self.bot.say(embed=embedError)
                    return
            else:
                noperm = discord.Embed(title=None, description=None, color=Error)
                noperm.add_field(name='Error', value='Are you sure you have permission to load ' + extension_name, inline=True)
                await self.bot.say(embed=noperm)


    @commands.command(pass_context=True)
    async def unload(self, ctx, extension_name : str):
        """Unloads an extension."""
        extension_name = extension_name.strip()
        if "cogs." not in extension_name:
            extension_name = "cogs." + extension_name # nico unload Owner => nico unload cogs.Owner
            if ctx.message.author.id in ownerID:
                if "Owner" in extension_name:
                    embed = discord.Embed(title=None, description=None, color=Error)
                    embed.add_field(name='Error', value=extension_name + " can't be unloaded.", inline=False)
                    await self.bot.say(embed=embed) # This obviously stops cogs.Owner from being disabled.
                else:
                    self.bot.unload_extension(extension_name)
                    embed = discord.Embed(title=None, description=None, color=OK)
                    embed.add_field(name=extension_name, value="Cog unloaded.")
                    await self.bot.say(embed=embed)
            else:
                noperm = discord.Embed(title=None, description=None, color=Error)
                noperm.add_field(name='Error', value='Are you sure you have enough permission to unload ' + extension_name, inline=True)
                await self.bot.say(embed=noperm)

    @commands.command(pass_context=True)
    async def pfp(self, ctx, args : str):
        if ctx.message.author.id in ownerID:
            args = args.strip()
            if 'default' in args:
                with open('default.png', 'rb') as f:
                    await self.bot.edit_profile(avatar=f.read())
                    embed = discord.Embed(title=None, description=None, color=OK)
                    embed.add_field(name='Profile', value='Profile Picture has changed.', inline=False)
                    await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def say(self, ctx, str : str, *args):
        str = str.strip()
        mesg = ' '.join(args)
        await self.bot.delete_message(ctx.message)
        if ctx.message.author.id in ownerID:
            if 'embed' in str:
                embed = discord.Embed(title=None, description=None, color=OK)
                embed.add_field(name='Say', value=mesg)
                await self.bot.say(embed=embed)
            if 'embed' not in str: # If embed is not in str
                mesg = str + ' ' +  mesg # Then mesg will be combined with str and mesg
                await self.bot.say(mesg) # And the bot will say the message the user wanted.
        else:
            embed = discord.Embed(title=None, description=None, color=Error)
            embed.add_field(name='Error', value='Are you sure you have enough permission to run this command?', inline=False)
            await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(Owner(bot))
