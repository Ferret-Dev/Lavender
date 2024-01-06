#DIFFUSION COG
#-imports-
import os
# filesystem
import discord
# discord api wrapper
from discord.ext import commands
# discord bot client with commands
import requests
# python http client library
import json
# json data module
import io
# file related input/output
import base64
# base64 encoding/decoding module
from PIL import Image, PngImagePlugin
# pillow libraries for image manipulation
from fractions import Fraction

print('diffusion cog online')
# prints cog status to terminal

#-cogs-
class diffusion_cog(commands.Cog):
# defines name of cog
  def __init__(self, bot):
  # initializes attributes of cog
    self.bot = bot
    # defines bot for the cog

  #-COMMANDS-
  @commands.command()
  async def gen(self, ctx):
  # triggers on 'gen' command
    if ctx.guild.id == 916526414017228800:
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_author(name='Your image is currently processing', icon_url=self.bot.user.avatar)
      deleteme = await ctx.reply(embed=embed)
      # defines 'deleteme' as a reply to the message context
      prompt = str(ctx.message.content.replace("!-gen ", ""))
      # defines 'prompt' as the message text without the command prefix
      payload = {"prompt": prompt, "steps": 20}
      # defines 'payload' using stable diffusions json parameters
      response = requests.post(url=f'http://192.168.0.234:7860/sdapi/v1/txt2img', json=payload)
      # defines 'response' as posting json data to the url for txt2img

      r = response.json()
      # defines 'r' as the json 'response'
      for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))
        # defines 'image' as decoded using base64
      png_payload = {"image": "data:image/png;base64," + i}
      # defines 'png_payload' as encoded using base64
      response2 = requests.post(url=f'http://192.168.0.234:7860/sdapi/v1/png-info', json=png_payload)
      # defines 'response2' as posting json data to the url for png-info

      pnginfo = PngImagePlugin.PngInfo()
      # defines 'pnginfo' as the png information retrieved through pillow
      pnginfo.add_text("parameters", response2.json().get("info"))
      # adds 'parameter' text to 'pnginfo'
      
      genauthor = str(ctx.message.author.id)
      genpath = './databases/diffusion/' + genauthor + '/'
      if os.path.exists(genpath):
        l=os.listdir(genpath)
        li=[int(x.split('.')[0]) for x in l]
        lastimg = max(li) + 1
        finalimgnum = str('%05d' % lastimg)
        imagename = finalimgnum + '.png'
        image.save(genpath + imagename, pnginfo=pnginfo)
        # saves 'image' as 'DiffusionOutput.png'
        outputimg = discord.File(genpath + imagename, filename=imagename)
        # defines 'outputimg' as file 'DiffusionOutput.png'
        await deleteme.delete()
        # deletes message 'deleteme'
        urlimg = 'attachment://' + imagename
        embed.set_author(name='Here\'s your image!', icon_url=self.bot.user.avatar)
        embed.set_image(url=urlimg)
        await ctx.reply(embed=embed, file=outputimg)
        # replies to original message context with 'outputimg'
      else:
        os.mkdir(genpath)
        firstimg = '00001.png'
        image.save(genpath + firstimg)
        outputimg = discord.File(genpath + firstimg, filename=firstimg)
        await deleteme.delete()
        urlimg = 'attachment://' + imagename
        embed.set_author(name='Here\'s your image!', icon_url=self.bot.user.avatar)
        embed.set_image(url=urlimg)
        await ctx.reply(embed=embed, file=outputimg)
    else:
      return

  @commands.command()
  async def upscale(self, ctx):
    if self.bot.is_owner(ctx.message.author.id):
      user = [438111061535621130, 952020078323449867, 837110690199502859]
      if ctx.message.author.id in user:
        if ctx.message.attachments:
          for image in ctx.message.attachments:
            imagepath = './cache/' + image.filename
            await image.save(imagepath)
            prompt = str(ctx.message.content.replace("!-upscale ", ""))
            payload = {"upscaling_resize": prompt, "upscaler_1": 'SwinIR_4x', "upscaling_crop": false}
            await ctx.reply('Image downloaded, checking resolution')
            img = Image.open(imagepath)
            width = img.width
            height = img.height
            await ctx.reply('Width is `' + str(width) + '`, height is `' + str(height) + '`. Aspect ratio is `' + str(Fraction(width/height)) + '`, or `' + str(width/height) + '`')

#-setup-
async def setup(bot):
  await bot.add_cog(diffusion_cog(bot))
  # adds 'autowan_cog' to list of cogs