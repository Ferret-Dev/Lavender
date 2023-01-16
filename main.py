#ALL IMPORTS
import os
# filesystem
import logging
# for error handling
import discord
# discord api wrapper
from dotenv import load_dotenv
# client secrets + keys
from discord.ext import commands
# discord bot client with commands
import asyncio
# library for doing time-based stuff

#DEFINITIONS + SETUP
load_dotenv()
# loads keys
TOKEN = os.getenv('D_TOKEN')
# grabs discord token from .env
intents = discord.Intents.all()
# specifies intents used by Lavender
bot = commands.Bot(command_prefix="!-", help_command=None, intents=intents)
# makes bot commands and enables all intents

#RUN BOT
discord.utils.setup_logging()
# for handling logs, I don't have the energy to fully grasp this right now

async def load_extensions():
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
    # cut off the .py from the file name
      await bot.load_extension(f"cogs.{filename[:-3]}")
      # loads all cogs in './cogs' directory

async def main():
  async with bot:
    await load_extensions()
    await bot.start(TOKEN)
asyncio.run(main())
# runs bot, obviously
