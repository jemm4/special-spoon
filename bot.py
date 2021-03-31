# bot.py

import os
from dotenv import load_dotenv
import random
from databasecontroller import DatabaseController
import discord

db = DatabaseController()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user.name} has connected to Discord!")


@client.event
async def on_message(message):
    # TODO: Make this more robust. I'm just trolilng with this
    id = message.author.id
    print(id)


client.run(TOKEN)
