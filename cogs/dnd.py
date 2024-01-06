#DIFFUSION COG
#-imports-
import os
# filesystem
import discord
# discord api wrapper
from discord.ext import commands
# discord bot client with commands
import random
import souldatabase

print('dnd cog online')
# prints cog status to terminal

#-dice bag-
dicebag = {
  '4': {'./dicebag/D4.png'},
  '6': {'./dicebag/D6.png'},
  '8': {'./dicebag/D8.png'},
  '10': {'./dicebag/D10.png'},
  '12': {'./dicebag/D12.png'},
  '20': {'./dicebag/D20.png'}
}
#discordfile = discord.File(iconfile),
#iconurl = 'attachment://' + iconfile

#-cogs-
class dnd_cog(commands.Cog):
# defines name of cog
  def __init__(self, bot):
  # initializes attributes of cog
    self.bot = bot
    # defines bot for the cog

  #-COMMANDS-
  @commands.command()
  async def roll(self, ctx, *, content:str):
  # triggers on 'gen' command
    dicenum = content
    if dicenum in dicebag:
      if dicenum not in ('6', '10'):
        icon = dicebag[dicenum]
        lavresponse = random.choice(souldatabase.dicesec1)
        rollnum = str(random.randint(1,int(dicenum)))
        response = ctx.message.author.display_name + ' rolled **' + rollnum + '** on a D' + dicenum + '. ' + lavresponse
        await ctx.reply(response)
      else:
        await ctx.reply('Numbers 6 and 10 don\'t work at the moment, please try again later')
    else:
      await ctx.reply('This command is for DND dice, and only works for numbers 4, 6, 8, 10, 12, and 20. Sorry!')

#-setup-
async def setup(bot):
  await bot.add_cog(dnd_cog(bot))
  # adds 'dnd_cog' to list of cogs