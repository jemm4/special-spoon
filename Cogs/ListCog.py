import discord
from discord.ext import commands
from DatabaseController import DatabaseController

class ListCog(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DatabaseController()

    # Commands
    @commands.slash_command(name="newlist", description="Create a list or multiple lists")
    async def new_list(
            self,
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

        listnames = listnames.replace(', ', " ").replace(',', ' ').split(' ')
        existingLists = []
        createdLists = []

        for listName in listnames:
            createdLists.append(listName) if self.db.create_new_list(listName, context.author.id) else existingLists.append(listName)

        await context.respond("{msg}".format(msg=await self.get_bot_output(createdLists, existingLists)))

    # Helpers
    async def get_bot_output(self, createdLists, existingLists):
        retval = ""
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
        return retval
