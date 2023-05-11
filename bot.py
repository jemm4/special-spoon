# bot.py

import os
import discord
from dotenv import load_dotenv

from DatabaseController import DatabaseController

db = DatabaseController()
bot = discord.Bot()


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(description="Create a list or multiple lists")
async def newlist(
        context: discord.ApplicationContext,
        listnames: discord.Option(
            description="The name of the list you want to add. If adding multiple lists, seperate with a comma or a space.",
            required=True
        )):
    #     """Makes a new list or lists and save it to the database
    #
    #         Parameters
    #         ----------
    #         context : discord.ApplicationContext (https://docs.pycord.dev/en/stable/api/application_commands.html#discord.ApplicationContext)
    #             Discord application command interaction context
    #         listnames :
    #             A list of names
    #
    #         Returns
    #         ----------
    #         [str]
    #             Messages for the bot to reply with
    #         """
    retval = ""
    listnames = listnames.replace(', ', " ").replace(',', ' ').split(' ')
    existingLists = []
    createdLists = []

    for listName in listnames:
        createdLists.append(listName) if db.createNewList(listName, context.author.id) else existingLists.append(
            listName)

    # Bot output result
    if len(existingLists) > 0:
        existingListsReply = "The following lists were not added because a list already exists with the name:\n"
        for l in existingLists:
            existingList = "**" + l + "**" + "\n"
            existingListsReply += existingList
        retval += existingListsReply

    if len(createdLists) > 0:
        createdListsReply = "The following lists were added:\n"
        for l in createdLists:
            createdList = "**" + l + "**" + "\n"
            createdListsReply += createdList
        retval += createdListsReply

    await context.respond("{msg}".format(msg=retval))


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
