import sqlite3
import os
from dotenv import load_dotenv

class DatabaseController:

    def __init__(self):
        load_dotenv()
        dbPath = os.getenv('DATABASE_PATH')

        # Database Connection
        self.con = sqlite3.connect(dbPath)

    def __del__(self):
        self.con.close()

    def createList(self, listName, creatorId):
        """Creates a new list if one with its name does not already exist

        Parameters
        ----------
        listName : str
            The name of the new list
        creatorId : int
            The discord id of the creator of the list

        Returns
        -------
        bool
            Whether the creation of the new list was successful
        """

        listName = listName.lower()

        if not self.listExists(listName):    
            cur = self.con.cursor()
            sql = "INSERT INTO list(creator_id, list_name) VALUES(?, ?)"
            params = (creatorId, listName)

            cur.execute(sql, params)   
            self.con.commit()
            return True

        return False


    def listExists(self, listName):
        cur = self.con.cursor()
        params = (listName,)
        sql = "SELECT * FROM list WHERE list_name=?"

        cur.execute(sql, params)
        result = cur.fetchone()

        if result == None:
            return False

        return True
