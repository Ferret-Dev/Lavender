import discord
from discord.ext import commands
import ffmpeg
import yt_dlp

#-cogs-
class audioremastered_cog(commands.Cog):
# defines the name of the cog ('test' in this case)
  def __init__(self, bot):
  # initializes attributes of cog
    self.bot = bot
    # defines what 'bot' is for the cog

  @commands.command()
  async def join(self, ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

  @commands.command()
  async def play(self, ctx):
    url = ctx.message.content.replace("!-play ", "")
    channel = ctx.author.voice.channel
    await channel.connect()

    ydl_opts = {'format': 'bestaudio'}
    ffmpeg_options = {'options': '-vn'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      song_info = ydl.extract_info(url, download=False)
      ctx.voice_client.play(discord.FFmpegPCMAudio(song_info["url"], **ffmpeg_options))

#setup
async def setup(bot):
  await bot.add_cog(audioremastered_cog(bot))
  # adds 'music_cog' to list of cogs