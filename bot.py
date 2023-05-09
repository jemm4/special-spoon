# bot.py

import os
from dotenv import load_dotenv
import random
from databasecontroller import DatabaseController
from discord.ext import commands
import discord

botPrefix = "-picker" # TODO: Get a real prefix??
db = DatabaseController()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=botPrefix, intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')



@bot.event
async def on_message(message):
    # TODO: Make this more robust. I'm just trolilng with this
    if message.content.startswith(botPrefix):
        botReplies = processMessages(message)

        for reply in botReplies:
            await message.reply(reply)

def processMessages(message):
    """Processes messages sent by users of the bot

        Parameters
        ----------
        message : discord.Message (https://discordpy.readthedocs.io/en/stable/api.html?highlight=message#discord.Message)
            Message sent by user

        Returns
        ----------
        [str]
            Messages for the bot to reply with
        """

    retval = []
    command = message.content.split()

    if len(command) == 1:
        return retval
    elif len(command) >= 2:
        if command[1].lower() == "newlist":
            # Everything after newlist is a list to be made, separated by space
            # TODO: probably move some of this logic into a seprate class so this extra logic isn't just sitting here
            newLists = command[2:]

            if len(newLists) == 0: # no lists added, missing list name
                retval.append("You need to specify a list name to add (i.e. -picker newlist booba)")
                return retval

            existingLists = []
            createdLists = []

            for list in newLists:
                createdLists.append(list) if db.createNewList(list, message.author.id) else existingLists.append(list)

            # Bot output result
            if len(existingLists) > 0:
                existingListsReply = "The following lists were not added because a list already exists with the name:\n"
                for l in existingLists:
                    existingList = "**" + l + "**" + "\n"
                    existingListsReply += existingList
                retval.append(existingListsReply)

            if len(createdLists) > 0:
                createdListsReply = "The following lists were added:\n"
                for l in createdLists:
                    createdList = "**" + l + "**" + "\n"
                    createdListsReply += createdList
                retval.append(createdListsReply)

        return retval


bot.run(TOKEN)
