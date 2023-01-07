#STATUS COG
#imports
import discord
from discord.ext import commands
from platform import python_version
import asyncio

print('status cog online')

#cogs
class status_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  #EVENT/LISTER
  @commands.Cog.listener()
  async def on_ready(self):
    #definitions for statistics
    server_number = str(len(self.bot.guilds))
    total_people = str(sum((guild.member_count) for guild in self.bot.guilds))
    ping_number = str(round(self.bot.latency*1000))
    py_version = str(python_version())
    #starting number for random list
    listnum = 0
    #list of statuses
    statuses = [
      'in ' + server_number + ' servers',
      'with your mom at night',
      'with ' + total_people + ' people',
      'please help me dear god',
      'at ' + ping_number + 'ms ping',
      'black jack. Or not.',
      'Lethal League Blaze',
      'on python v' + py_version,
      'with your junk ;)',
      '!-help for more info',
      'with some thick knots UwU',
      'Changed']
    #running random list
    while not self.bot.is_closed():
      status = statuses[listnum]
      await self.bot.change_presence(activity=discord.Game(name=status))
      await asyncio.sleep(10)
      listnum += 1
      if listnum >= 11:
        listnum = 0
#setup
async def setup(bot):
  await bot.add_cog(status_cog(bot))
