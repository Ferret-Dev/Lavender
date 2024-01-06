#COMMANDS COG
#-imports-
import os
# filesystem
import discord
# discord api wrapper
from discord.ext import commands
# discord bot client with commands
from discord.ext.commands import has_permissions
# allows checking for guild permissions
import random
# python random library
import souldatabase
# lavenders response database
from dotenv import load_dotenv
# environment secrets
from time import sleep
# imports 'sleep' from pythons time library
from platform import python_version
# allows displaying python version
from PIL import Image
# imports image manipulation from Pillow
from apnggif import apnggif
# allows converting apng to gif
import rasterio
import glob

print('commands cog online')
# prints cog status to terminal

#-cogs-
class commands_cog(commands.Cog):
# defines name of cog
  def __init__(self, bot):
  # initializes attributes of cog
    self.bot = bot
    # defines bot for the cog

  #-COMMANDS-
  @commands.command()
  async def help(self, ctx):
    helpcmd = {
      '!-hug': {'Use this command to hug another user with `!-hug [@user]`'},
      '!-info': {'Use this command to learn more about Lavender\'s server'},
      '!-pfp': {'Use this command to grab your profile picture, or use it while mentioning a user with `!-pfp [@user]` to grab theirs.'},
      '!-ping': {'Use this command to see Lavender\'s connection latency'},
      '!-quote': {'Use this command to generate an AI inspirational quote through Inspirobot'},
      '!-ss': {'Use this command to screenshot a message by replying to the target message with `!-ss`'},
      '!-steal': {'Use this command with custom emojis to return an image with `!-steal [emoji]`'},
      '!-voremsg': {'Use this command to delete messages in a channel up to a certain amount with `!-voremsg [number]`'},
      '!-suggest': {'Use this command to suggest a feature or bug fix with `!-suggest [text]`'}
    }
    response = souldatabase.help
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    embed.set_author(name=random.choice(response), url=self.bot.user.avatar)
    commandlist = []
    badcommands = ['!-help', '!-dl', '!-pat', '!-upscale', '!-ferret', '!-save', '!-wan', '!-invite', '!-unload', '!-updatepfp', '!-play', '!-coglist', '!-roll', '!-gen', '!-join', '!-test2', '!-suggest', '!-serverlist']
    for command in self.bot.commands:
      commandlist.append('!-' + command.name)
    for i in badcommands:
      commandlist.remove(i)
    commandlist.sort()
    commandlist.insert(0, '!-help')
    finallist = '\n'.join(commandlist)
    embed.description = finallist
    await ctx.reply(embed=embed)
  
  @commands.command()
  async def pfp(self, ctx):
    response = souldatabase.pfp
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    if ctx.message.mentions:
      for user in ctx.message.mentions:
        embed.set_author(name = random.choice(response), icon_url=self.bot.user.avatar)
        embed.set_image(url=user.avatar)
        embed.set_footer(text=user.name)
        await ctx.reply(embed=embed)
    else:
      embed.set_author(name = random.choice(response), icon_url=self.bot.user.avatar)
      embed.set_image(url=ctx.author.avatar)
      embed.set_footer(text=ctx.author.name)
      await ctx.reply(embed=embed)

  @commands.command()
  async def ss(self, ctx):
    if ctx.message.reference == None:
      response = souldatabase.ss_1
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_author(name=str(random.choice(response)), icon_url=self.bot.user.avatar)
      await ctx.reply(embed=embed)
    else:
      ref = await ctx.fetch_message(ctx.message.reference.message_id)
      pfp = ref.author.avatar
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_author(name=str(ref.author), icon_url=str(pfp))
      embed.title = str(ref.content)
      stamp = ref.created_at
      time = stamp.strftime(r"%-I:%M %p")
      date = stamp.strftime(r'%-m/%-d/%y')
      embed.set_footer(text='Sent ' + str(date) + ' at ' + str(time) + ' UTC')
      if len(ref.attachments) > 0:
        for attachment in ref.attachments:
          if 'image' in attachment.content_type:
            embed.set_image(url=str(ref.attachments[0].url))
            await ctx.reply(embed=embed)
            if ctx.message.guild.id == 1137627580699250748:
              quotechannel = self.bot.get_channel(1148127769952256060)
              await quotechannel.send(embed=embed)
            else:
              return
          else:
            response = souldatabase.ss_2
            embed = discord.Embed()
            embed.colour = 0xffb3f7
            embed.set_author(name=str(random.choice(response)), icon_url=self.bot.user.avatar)
            await ctx.reply(embed=embed)
      else:
        await ctx.reply(embed=embed)
        if ctx.message.guild.id == 1137627580699250748:
          quotechannel = self.bot.get_channel(1148127769952256060)
          await quotechannel.send(embed=embed)
        else:
          return

  @commands.command()
  async def suggest(self, ctx, content:str = None):
    if self.bot.is_owner(ctx.message.author.id):
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      if content is not None:
        content = ' '.join(content)
        if len(content) > 127:
          response = souldatabase.suggest
          embed.set_author(name = str(random.choice(response)))
          await ctx.reply(embed=embed)
        else:
          embed.set_author(name = ctx.author.name + ' suggested \"' + content + '.\"', icon_url=ctx.author.avatar)
          await ctx.reply(embed=embed)
          user = await self.bot.fetch_user('438111061535621130')
          embed.set_author(name = ctx.author.name + ' suggested \"' + content + '\"', icon_url=ctx.author.avatar)
          await user.send(embed=embed)
      else:
        await ctx.reply('Nothing was suggested')
    else:
      await ctx.reply('Sorry, this command is currently undergoing maintenance. Please check again later.')
    
  @commands.command()
  async def invite(self, ctx):
    response = souldatabase.invite
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    embed.set_author(name = str(random.choice(response)),icon_url=self.bot.user.avatar)
    embed.title = 'Invite Link'
    embed.url = 'https://discord.com/api/oauth2/authorize?client_id=814365204619329576&permissions=8&scope=bot'
    await ctx.reply(embed=embed)

  @commands.command()
  async def ping(self, ctx):
    response = souldatabase.ping
    try:
      rounded = round(self.bot.latency*1000)
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_author(name='Pong, bitch. Latency is around ' + str(rounded) + 'ms, ' + str(random.choice(response)),icon_url=self.bot.user.avatar)
      await ctx.reply(embed=embed)
    finally:
      return

  @commands.command()
  async def hug(self, ctx):
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    if ctx.message.mentions:
      for user in ctx.message.mentions:
        if user.id == ctx.author.id:
          response = souldatabase.hugself
          embed.set_author(name=str(random.choice(response)), icon_url=self.bot.user.avatar)
          await ctx.reply(embed=embed)
        else:
          embed.set_author(name=user.name + ' has been hugged by ' + ctx.author.name + ' UwU', icon_url=user.avatar)
          await ctx.reply(embed=embed)
    else:
      response = souldatabase.hugblank
      embed.set_author(name=str(random.choice(response)), icon_url=self.bot.user.avatar)
      await ctx.reply(embed=embed)

  @commands.command()
  async def updatepfp(self, ctx):
    if self.bot.is_owner(ctx.message.author.id):
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      if self.bot.is_owner(ctx.message.author.id):
        if not ctx.message.attachments:
          embed.set_author(name='There\'s no image', icon_url=self.bot.user.avatar)
          await ctx.reply(embed=embed)
        else:
          attachment = discord.Attachment
          for attachment in ctx.message.attachments:
            await attachment.save('./cache/newpfp.png')
          newpfp = discord.File('./cache/newpfp.png')
          with open('./cache/newpfp.png', "rb") as file:
            read_pfp = file.read()
            await self.bot.user.edit(avatar = read_pfp)
          embed.set_author(name='Profile picture has been changed', icon_url=self.bot.user.avatar)
          await ctx.reply(embed=embed)
      else:
        response = souldatabase.not_owner
        embed.set_author(name=random.choice(response), icon_url=self.bot.user.avatar)
        await ctx.reply(embed=embed)

  @commands.command()
  async def steal(self, ctx, emoji: discord.PartialEmoji = None):
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    embed.set_author(name='Here, you dick.', icon_url=self.bot.user.avatar)
    msgid = []
    if ctx.message.reference:
      msgid.append(ctx.message.reference.message_id)
    else:
      msgid.append(ctx.message.id)
    context = await ctx.fetch_message(*msgid)
    if context.stickers:
      for sticker in context.stickers:
        if str(sticker.format) == 'StickerFormatType.apng':
          stickerfile = './cache/sticker.png'
          await sticker.save(stickerfile)
          apnggif(stickerfile)
          os.remove(stickerfile)
          newstickerfile = './cache/sticker.gif'
          outputimg = discord.File(newstickerfile, filename='sticker.gif')
          urlimg = 'attachment://sticker.gif'
          embed.set_image(url=urlimg)
          await context.channel.send(embed=embed, file=outputimg)
          os.remove(newstickerfile)
        else:
          embed.set_image(url=sticker.url)
          await context.channel.send(embed=embed)
    else:
      embed.set_image(url=emoji.url)
      await context.channel.send(embed=embed)

  @commands.command()
  @has_permissions(administrator=True, manage_messages=True)
  async def voremsg(self, ctx, *, content:str):
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    number = int(content) + 1
    await ctx.channel.purge(limit=number)
    embed.set_author(name=str(number) + ' messages have been vored', icon_url=self.bot.user.avatar)
    await ctx.channel.send(embed=embed, delete_after=5)

  @commands.command()
  async def info(self, ctx):
    try:
      server_number = str(len(self.bot.guilds))
      total_people = str(sum((guild.member_count) for guild in self.bot.guilds))
      ping_number = str(round(self.bot.latency*1000))
      py_version = str(python_version())
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_author(name='Really? No privacy whatsoever?', icon_url=self.bot.user.avatar)
      embed.add_field(name='Systems Info:', value='GPU | *Intel HD 3000*\nCPU  | *Intel Core i5-2520M*\nRAM  | *4GB*\nOS | *Arch Linux*\nPython Version | *' + py_version + '*', inline=False)
      embed.add_field(name='Statistics:', value='Servers  | ' + server_number + '\nUsers  | ' + total_people + '\nPing | ' + ping_number, inline=False)
      await ctx.reply(embed=embed)
    finally:
      return
  
  @commands.command()
  async def serverlist(self, ctx):
    if self.bot.is_owner(ctx.message.author.id):
      guildlist = []
      for guild in self.bot.guilds:
        guildlist.append(guild.name)
      await ctx.reply(str(guildlist))

  @commands.command()
  async def pat(self, ctx):
    if self.bot.is_owner(ctx.message.author.id):
      await ctx.reply(str(ctx.message.guild.id))

  @commands.command()
  async def test2(self, ctx):
    if self.bot.is_owner(ctx.message.author.id):
      imgextlist = ['.png', '.jpg', '.jpeg', '.webp']
      if ctx.message.attachments:
        for file in ctx.message.attachments:
          for ext in imgextlist:
            if file.filename.endswith(ext):
              await file.save('./databases/ferretimgs/' + file.filename)
              with Image.open('./databases/ferretimgs/' + file.filename) as im:
                #await ctx.reply('**Original Metadata:**\n' + str(im.info))
                #fields_to_keep = ('transparency')
                #exif_fields = list(im.info.keys())
                #for k in exif_fields:
                #  if k not in fields_to_keep:
                #    del im.info[k]
                #    im.save('./databases/ferretimgs/' + file.filename, format='PNG')
                #old_file = rasterio.open('./databases/ferretimgs/' + file.filename)
                #profile=old_file.profile
                #data=old_file.read()
                #with rasterio.open('./databases/ferretimgs/' + file.filename,'w',**profile) as dst:
                #  dst.update_tags(a='1', b='2')
                #  dst.write(data)
                #  dst.close()
                im=rasterio.open('./databases/ferretimgs/' + file.filename)
                await ctx.reply('**The image\'s Rasterio metadata is:** `' + str(im.tags()) + '`')
                #await ctx.reply(file=discord.File('./databases/ferretimgs/' + file.filename))
      else:
        await ctx.reply('no attachment')

  @commands.command()
  async def save(self, ctx):
    if self.bot.is_owner(ctx.message.author.id):
      imgextlist = ['.png', '.jpg', '.jpeg', '.webp']
      if ctx.message.attachments:
        for file in ctx.message.attachments:
          for ext in imgextlist:
            if file.filename.endswith(ext):
              databasepath = './databases/ferretimgs/'
              l=os.listdir(databasepath)
              li=[int(x.split('.')[0]) for x in l]
              lastimg = max(li) + 1
              finalimgnum = str('%05d' % lastimg)
              imagename = finalimgnum + '.png'
              await file.save(databasepath + imagename)
              with Image.open(databasepath + imagename) as im:
                fields_to_keep = ('transparency')
                exif_fields = list(im.info.keys())
                for k in exif_fields:
                  if k not in fields_to_keep:
                    del im.info[k]
                    im.save(databasepath + imagename, format='PNG')
                old_file = rasterio.open(databasepath + imagename)
                profile=old_file.profile
                data=old_file.read()
                with rasterio.open(databasepath + imagename,'w',**profile) as dst:
                  dst.update_tags(name='Joey', owner='u/Acerichor', link='https://www.reddit.com/r/ferrets/comments/15wjmi7/joey_our_noodle_of_7_years_had_crossed_the/')
                  dst.write(data)
                  dst.close()
                #os.remove(databasepath + imagename + '.aux.xml')
                await ctx.reply(file=discord.File(databasepath + imagename))
    
  @commands.command()
  async def ferret(self, ctx):
    if self.bot.is_owner(ctx.message.author.id):
      databasepath = './databases/ferretimgs/'
      images = glob.glob(databasepath + "*.png")
      random_image = random.choice(images)
      urlimg = 'attachment://' + random_image
      im=rasterio.open(random_image)
      tags = im.tags()
      imgowner = tags['owner']
      imgname = tags['name']
      imglink = tags['link']
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_author(name='Picture of ferret named ' + imgname + ' from database')
      embed.description = 'Posted by ' + imgowner + ' on [' + imglink + '](r/Ferrets)'
      embed.set_footer(text='Posted by ' + imgowner + ' on ')
      filename = os.path.splitext(random_image)[0]
      outputimg = discord.File(random_image, filename=filename + '.png')
      embed.set_image(url=urlimg)
      await ctx.reply(embed=embed, file=outputimg)

#setup
async def setup(bot):
  await bot.add_cog(commands_cog(bot))