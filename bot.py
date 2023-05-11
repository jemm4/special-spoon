# bot.py

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from Cogs.ListCog import ListCog

bot = commands.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot.add_cog(ListCog(bot))
bot.run(TOKEN)
