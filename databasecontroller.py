import sqlite3
import os
from dotenv import load_dotenv


class DatabaseController:
    def __init__(self):
        load_dotenv()
        dbPath = os.getenv("DATABASE_PATH")

        # Database Connection
        self.con = sqlite3.connect(dbPath)

    def __del__(self):
        self.con.close()

    def CreateList(self, listName: str, creatorId: int):
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

        if not self.ListExists(listName):
            cur = self.con.cursor()
            sql = "INSERT INTO list(creator_id, list_name) VALUES(?, ?)"
            params = (creatorId, listName)

            cur.execute(sql, params)
            self.con.commit()
            return True

        return False

    def ListExists(self, listName: str):
        """Determines if a list exists in the list table

        Parameters
        ----------
        listName : str
            The name of the list to search for

        Returns
        -------
        bool
            Whether the list exists
        """
        cur = self.con.cursor()

        params = (listName,)
        sql = "SELECT * FROM list WHERE list_name=?"

        cur.execute(sql, params)

        return False if cur.fetchone() == None else True

    def CategoryExists(self, categoryName: str):
        """Determines if a category exists in the item_categories table

        Parameters
        categoryName : str
            The name of the item category to search for

        Returns
        -------
        bool
            Whether the category exists
        """
        cur = self.con.cursor()

        params = (categoryName,)
        sql = "SELECT * FROM item_categories WHERE category_name=?"

        cur.execute(sql, params)

        return False if cur.fetchone() == None else True

    def ItemExists(self, itemName: str):
        """Determines if an item exists in the item table

        Parameters
        ----------
        itemName : str
            The name of the item to search for

        Returns
        -------
        bool
            Whether the item exists
        """
        cur = self.con.cursor()

        params = (itemName,)
        sql = "SELECT * FROM item WHERE item_name=?"

        cur.execute(sql, params)

        return False if cur.fetchone() == None else True

    def AddItemToDatabase(self, itemName: str, categoryName: str):
        """Creates a new item in the item table, if one with its name does not already exist

        Parameters
        ----------
        itemName : str
            The name of the new item
        categoryName : str
            The category name of the item being added

        Returns
        -------
        bool
            Whether the addition of the new item was successful
        """
        categoryId = self.GetCategoryId(categoryName)

        if not self.ItemExists(itemName):
            cur = self.con.cursor()

            sql = "INSERT INTO item (item_name, category_id) VALUES (?, ?)"
            params = (
                itemName,
                categoryId,
            )

            cur.execute(sql, params)
            self.con.commit()

        return True if self.ItemExists(itemName) else False

    def GetCategoryId(self, categoryName: str):
        """Retrieves the category id of the given category if it exists. Otherwise, it
        adds the category and retrieves the category id

        Parameters
        ----------
        categoryName : str
            The name of the category to search

        Returns
        -------
        categoryId : str
            The category id of the passed in category name
        """
        if not self.CategoryExists(categoryName):
            self.AddCategoryToDatabase(categoryName)

        cur = self.con.cursor()
        params = (categoryName,)

        sql = "SELECT category_id FROM item_categories WHERE category_name=?"

        cur.execute(sql, params)
        (categoryId,) = cur.fetchone()

        return str(categoryId)

    def AddCategoryToDatabase(self, categoryName: str):
        """Creates a new category in the item_categories table, if one with its name does not already exist

        Parameters
        ----------
        categoryName : str
            The name of the category being added

        Returns
        -------
        bool
            Whether the addition of the new category was successful
        """
        if not self.CategoryExists(categoryName):
            cur = self.con.cursor()

            sql = "INSERT INTO item_categories (category_name) VALUES (?)"
            params = (categoryName,)

            cur.execute(sql, params)
            self.con.commit()

        return True if self.CategoryExists(categoryName) else False
