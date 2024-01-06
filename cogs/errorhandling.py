import discord
from discord.ext import commands

print('errorhandling cog online')

#-cogs-
class errorhandling_cog(commands.Cog):
# defines name of cog
  def __init__(self, bot):
  # initializes attributes of cog
    self.bot = bot
    # defines bot for the cog

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
      await ctx.send('Wrong command, dipshit')
    elif isinstance(error, discord.ext.commands.errors.MissingPermissions):
      await ctx.send('You do not have the permissions to execute this command')
    else:
      raise error

#-setup-
async def setup(bot):
  await bot.add_cog(errorhandling_cog(bot))
  # adds 'autowan_cog' to list of cogs