# bot.py

import random
from databasecontroller import DatabaseController
import discord # TODO: ACTUALLY USE THE BOT SOMEHOW

db = DatabaseController()


def getRandomActivity():
    activityRows = db.getAllActivities()
    result = random.choice(activityRows)
    return result[1] # 0 = activity_id, 1 = activity_name



if __name__ == "__main__":
    print(getRandomActivity())