#INSPIROBOT COG
#general imports
import discord
from discord.ext import commands
#inspirobot imports
import inspirobot

print('inspirobot cog online')

#cogs
class inspirobot_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  #COMMANDS
  @commands.command()
  async def quote(self, ctx):
    quote = inspirobot.generate()
    embed = discord.Embed()
    embed.colour = 0x00ff00
    embed.set_author(name='Here\'s your quote, ' + ctx.author.name + '!',icon_url='https://inspirobot.me/website/images/inspirobot-dark-green.png')
    embed.set_image(url=str(quote))
    embed.set_footer(text='Generated from inspirobot.me')
    await ctx.reply(embed=embed)

#setup
async def setup(bot):
  await bot.add_cog(inspirobot_cog(bot))
