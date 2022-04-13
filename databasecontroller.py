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

    def createNewList(self, listName, creatorId):
        """Creates a new list

        Parameters
        ----------
        listNames : str
            Name of new list
        creatorId : int
            The discord id of the creator of the list
        """
        
        sql = "INSERT INTO list(creator_id, list_name) VALUES(?, ?);"
        values = (creatorId, listName)
        #values = [(creatorId, name) for name in listNames]
        cur = self.con.cursor()
        cur.execute(sql, values)
        self.con.commit()
        result = cur.fetchone()
        print(result)
        """
            tempSql = "INSERT INTO list(creator_id, list_name) VALUES(?, ?);"
        listName = listName.lower()

        if not self.listExists(listName):    
            cur = self.con.cursor()
            sql = "INSERT INTO list(creator_id, list_name) VALUES(?, ?)"
            params = (creatorId, listName)

            cur.execute(sql, params)   
            self.con.commit()
            return True

        return False
        """


    def listExists(self, listName):
        """Checks if a list already exists

        Parameters
        ----------
        listNames : str
            Name of list

        Returns
        ----------
        bool
            True if list exists, false otherwise
        """
        cur = self.con.cursor()
        params = (listName,)
        sql = "SELECT * FROM list WHERE list_name=?"

        cur.execute(sql, params)
        result = cur.fetchone()

        if result == None:
            return False

        return True
