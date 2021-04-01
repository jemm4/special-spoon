# bot.py

import os
from dotenv import load_dotenv
import random
from databasecontroller import DatabaseController
from discord.ext import commands

db = DatabaseController()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="?")


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.event
async def on_message(message):
    # TODO: Make this more robust. I'm just trolilng with this
    id = message.author.id
    print(id)


bot.run(TOKEN)
