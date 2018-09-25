import os

__cogs__ = [
    'cogs.noflippedtables'
] # These cogs actually make the bot have commands (except noflippedtables and ready).
# Don't remove any of these unless you know what you're doing.

__token__ = os.environ.get("Token") # This is a required field for the bot to login.

__git__ = "https://github.com/AgentHi5/nico-yazawa" # This is not a required field but you will get an error on start.
# A GitHub url is NOT required. The bot doesn't look for it. So the message could be like "Icy Minions!"
