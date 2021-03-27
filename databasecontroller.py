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

    def addActivity(self, name):
        sql = f"INSERT INTO activity(name) VALUES({name.lower()})"
        cur = self.con.cursor()

        cur.execute(sql)
        con.commit()

    def removeActivity(self, name):
        sql = f"DELETE FROM activity WHERE name = ({name.lower()})"
        cur = self.con.cursor()

        cur.execute(sql)
        con.commit()

    def getAllActivities(self):
        sql = "SELECT * FROM activity"
        cur = self.con.cursor()

        rows = cur.execute(sql).fetchall()
        return rows




    
    