#COGLOADER COG
#imports
import discord
from discord.ext import commands

print('cogloader cog online')

#cogs
class cogloader_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  #COMMANDS
  @commands.command()
  async def unload(self, ctx):
    extension = str(ctx.message.content.replace("!-unload ", ""))
    await self.bot.unload_extension(f"cogs.extension")
    await ctx.reply('try it now')

  @commands.command()
  async def coglist(self, ctx):
    online_cogs = []
    offline_cogs = []

    loaded_cogs = set(self.bot.cogs.keys())
    all_cogs = set(self.bot.extensions.keys())

    online_cogs = loaded_cogs.intersection(all_cogs)
    offline_cogs = all_cogs - online_cogs
    
    online_embed = discord.Embed(title="Online Cogs", description="\n".join(online_cogs), color=discord.Color.green())
    offline_embed = discord.Embed(title="Offline Cogs", description="\n".join(offline_cogs), color=discord.Color.red())

    await ctx.send(embed=online_embed)
    await ctx.send(embed=offline_embed)

#setup
async def setup(bot):
  await bot.add_cog(cogloader_cog(bot))