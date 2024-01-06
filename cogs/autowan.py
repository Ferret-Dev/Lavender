#AUTOWAN COG
#-imports-
import discord
# discord api wrapper
from discord.ext import commands
# discord bot client with commands
import requests
# python http client library

print('autowan cog online')
# prints cog status to terminal

#-cogs-
class autowan_cog(commands.Cog):
# defines name of cog
    def __init__(self, bot):
    # initializes attributes of cog
        self.bot = bot
        # defines bot for the cog

    #-COMMANDS-
    @commands.command()
    async def wan(self, ctx):
    # triggers on 'wan' command
        if ctx.author.id == 438111061535621130:
        # checks if author is me
            user = await self.bot.fetch_user('438111061535621130')
            # defines 'user' as my ID
            response = requests.get('https://checkip.amazonaws.com').text.strip()
            # defines 'response' as the string received from the http request
            await user.send(response)
            # sends DM to 'user'
        else:
            await ctx.reply()

#-setup-
async def setup(bot):
    await bot.add_cog(autowan_cog(bot))
    # adds 'autowan_cog' to list of cogs