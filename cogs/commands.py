#COMMANDS COG
#imports
import discord
from discord.ext import commands
import random

print('commands cog online')

#cogs
class commands_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  #COMMANDS
  @commands.command()
  async def pfp(self, ctx):
    response = ['Here you go, I guess', 'You asked for a pfp?', 'Damn, that pfp kinda ugly tho', 'I mean, I\'m not gonna judge, but...', 'Thats the best image you have?', 'That\'s not the pic I would have chosen', 'I\'d find a better picture if I were you.', 'Jesus, thats the image you wanted to represent you?', 'I might have to sue for endangerment after seeing that', 'Make better personal choices in the future.']
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    if ctx.message.mentions:
      for user in ctx.message.mentions:
        embed.set_author(name = str(random.choice(response)),icon_url=self.bot.user.avatar)
        embed.set_image(url=user.avatar)
        embed.set_footer(text=str(user.name) + '#' + user.discriminator)
        await ctx.reply(embed=embed)
    else:
      embed.set_author(name = str(random.choice(response)),icon_url=self.bot.user.avatar)
      embed.set_image(url=ctx.author.avatar)
      embed.set_footer(text=str(ctx.author))
      await ctx.reply(embed=embed)

  @commands.command()
  async def testlol(self, ctx):
    await ctx.reply('here')
    
  @commands.command()
  async def ss(self, ctx):
    if ctx.message.reference == None:
      response = ['Reply to a message you fucking idiot', 'The command really isn\'t that difficult.', 'Jesus dude, select a fucking message already!', 'Do you want me to screenshot a message or just blank fucking space?', 'Your supposed to SELECT A MESSAGE', 'No, thats fine. I didn\'t want to see the message anyways.', 'SELECT A MESSAGE ALREADY', 'I\'ll wait.', 'Theres a little reply button next to messages. Click it.', 'Are you ok? Is the command really that hard to execute?']
      embed = discord.Embed()
      embed.colour = 0xffb3f7
      embed.set_author(name=str(random.choice(response)), icon_url=self.bot.user.avatar)
      await ctx.reply(embed=embed)
    else:
      ref = await ctx.fetch_message(id=ctx.message.reference.message_id)
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
          else:
            response = ['I can\'t take a screenshot of it if its not a picture.', 'I swear to god if theres no image in that picture...', 'Listen here fucker, I won\'t screenshot any files that aren\'t images.', 'I see a file, but no picture. Try something else.', 'Really? Do I look like I can capture moving images?', 'Can\'t do that.', 'Are you fucking dumb? I can only screenshot pictures, not any other file.', 'Nope fuck off']
            embed = discord.Embed()
            embed.colour = 0xffb3f7
            embed.set_author(name=str(random.choice(response)), icon_url=self.bot.user.avatar)
            await ctx.reply(embed=embed)
      else:
        await ctx.reply(embed=embed)

  @commands.command()
  async def suggest(self, ctx):
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    embed.set_author(name = ctx.author.name + ' suggested \"' + str(ctx.message.content.replace("!-suggest ", "")) + '.\" What the fuck is that supposed to mean? You think you have better ideas than I do? Fuck outta here.', icon_url=ctx.author.avatar)
    await ctx.reply(embed=embed)
    
    user = await self.bot.fetch_user('438111061535621130')
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    embed.set_author(name = str(user.name) + '#' + user.discriminator + ' suggested \"' + ctx.message.content.replace("!-suggest ", "") + '\"')
    await user.send(embed=embed)
  
  @commands.command()
  async def invite(self, ctx):
    response = ['Here. Don\'t invite me to some dumb ass servers.', 'Use it wisely', '*That\'s your best pickup line?*', 'I dont give this out to just anyone.', 'Spread the word of god', 'These assholes better be worth joining...', 'Who said I wanted to join?', 'No.', 'Why me? Theres hundreds of other bots.', 'Fine. I\'m not bringing any snacks though.']
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    embed.set_author(name = str(random.choice(response)),icon_url=self.bot.user.avatar)
    embed.title = 'Invite Link'
    embed.url = 'https://discord.com/api/oauth2/authorize?client_id=814365204619329576&permissions=8&scope=bot'
    await ctx.reply(embed=embed)

  @commands.command()
  async def ping(self, ctx):
    response = ['not that it should really matter to you.', 'if you really have to know.', 'you fucking idiot.', 'which should be on par with how long you last in bed.', 'get some better fucking wifi.', 'your lucky I\'m still running.', 'but it\'d be faster if you bought me a server.']
    rounded = round(self.bot.latency*1000)
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    embed.set_author(name='Pong, bitch. Latency is around ' + str(rounded) + 'ms, ' + str(random.choice(response)),icon_url=self.bot.user.avatar)
    await ctx.reply(embed=embed)

  @commands.command()
  async def help(self, ctx):
    response = ['Figured you would have remembered these by now.', 'Come on, these aren\'t that hard to remember.', 'Are you fucking dumb?', 'Of course you of all people need help.', 'How about you get off discord and go help some bitches?', 'Pathetic.', 'The answer is RIGHT THERE', 'Really? This is simple stuff. Come on dude.', 'Aw, is someone gonna cry? Gonna piss your pants? Maybe cum?', 'Well that\'s kinda pathetic.']
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    embed.set_author(name=str(random.choice(response)), icon_url=self.bot.user.avatar)
    embed.description = '!-help\n!-ping\n!-invite\n!-ss\n!-pfp\n!-quote\n!-hug'
    await ctx.reply(embed=embed)

  @commands.command()
  async def hug(self, ctx):
    response = ['Hey asshole, you\'re supposed to hug someone other than yourself.', 'Find someone to hug ya dickhead.', 'Select someone, obviously.', 'Really? Not even gonna say who you want to hug?', 'Choose someone dumbass', 'This command is pretty self explanatory. Mention someone.', 'You need to @ someone to use this command dude', 'Really? Is this command just too complicated for you?', 'Come on. Do it right.', '...Who? Who do you want to hug? For fucks sake.']
    embed = discord.Embed()
    embed.colour = 0xffb3f7
    if ctx.message.mentions:
      for user in ctx.message.mentions:
        embed.set_author(name=user.name + ' has been hugged by ' + ctx.author.name + ' UwU', icon_url=user.avatar)
        await ctx.reply(embed=embed)
    else:
      embed.set_author(name=str(random.choice(response)), icon_url=self.bot.user.avatar)
      await ctx.reply(embed=embed)

  #Leave server
  @commands.command()
  async def leaveserver(self, ctx):
    await ctx.message.guild.leave()
    
#setup
async def setup(bot):
  await bot.add_cog(commands_cog(bot))
