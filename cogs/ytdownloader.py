import discord
from discord.ext import commands
import os
from yt_dlp import YoutubeDL

#-cogs-
class ytdownloader_cog(commands.Cog):
# defines name of cog
  def __init__(self, bot):
  # initializes attributes of cog
    self.bot = bot
    # defines bot for the cog

  @commands.command()
  async def dl(self, ctx):
    await ctx.channel.send('Downloading file now')

    url = ctx.message.content.replace("!-dl ", "")
    ydl_opts = {
    'format': 'bestaudio/best',  # Download the best quality audio
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # Use FFmpeg to extract audio
        'preferredcodec': 'mp3',      # Convert to mp3 format
        'preferredquality': '192',    # Set the quality of the MP3
    }],
    'outtmpl': 'cache/audiofile.%(ext)s',  # Name the file
    }
    with YoutubeDL(ydl_opts) as ydl:
      info_dict = ydl.extract_info(url, download=True)
      title = info_dict.get('title', None).replace('/', '-')

      oldaudio = os.path.join('./cache/', 'audiofile.mp3')
      newaudio = os.path.join('./cache/', title + '.mp3')
      os.rename(oldaudio, newaudio)
      finalaudio = './cache/' + title + '.mp3'

      await ctx.channel.send('Heres your file, you perv.')
      await ctx.channel.send(file=discord.File(finalaudio))
      os.remove(finalaudio)

async def setup(bot):
  await bot.add_cog(ytdownloader_cog(bot))
  # adds 'autowan_cog' to list of cogs