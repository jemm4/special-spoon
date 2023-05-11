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

    def create_new_list(self, listName: str, creatorId: int):
        """Creates a new list

        Parameters
        ----------
        listNames : str
            Name of new list
        creatorId : int
            The discord id of the creator of the list

        Returns
        ----------
        bool
            True if list was successfully created. False otherwise
        """

        if not self.list_exists(listName):
            sql = "INSERT INTO list(creator_id, list_name) VALUES(?, ?);"
            params = (creatorId, listName)
            cur = self.con.cursor()
            cur.execute(sql, params)
            self.con.commit()
            return True

        return False


    def list_exists(self, listName: str):
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

        return False if cur.fetchone() == None else True
