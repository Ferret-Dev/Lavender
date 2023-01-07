#STABILITY COG
#imports
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import io
import warnings

from IPython.display import display
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

KEY = os.getenv('STABILITY_KEY')
stability_api = client.StabilityInference(
    key=KEY, 
    verbose=True,)

print('stability cog online')

#cogs
class stability_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  #COMMANDS
  @commands.command()
  async def sd(self, ctx):

    deleteme = await ctx.reply('Your image is currently processing')
    words=ctx.message.content.replace("!-sd ", "")
    
    answers = stability_api.generate(prompt=str(words))
    
    for resp in answers:
      for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FILTER:
          warnings.warn("Your request activated the API's safety filters and could not be processed, please modify the prompt and try again.")
        if artifact.type == generation.ARTIFACT_IMAGE:
          img = Image.open(io.BytesIO(artifact.binary))
          display(img)
          img.save('image.png')
          embed = discord.Embed()
          embed.colour = 0xffb3f7
          embed.set_author(name='Here\'s your image!')
          file = discord.File('./image.png', filename='image.png')
          embed.set_image(url="attachment://image.png")
          await deleteme.delete()
          await ctx.reply(embed=embed, file=file)

#setup
async def setup(bot):
  await bot.add_cog(stability_cog(bot))
