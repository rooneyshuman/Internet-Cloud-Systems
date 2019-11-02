"""
Flask app to store and retrieve a list of bubble tea shops
Data is stored in a SQLite database that looks something like the following:

+------+--------------+----------+-------+-------+-----------+------------+--------------+-------------+------+--------+
| Nam  | Address      | City     | State | Zip   | Open Hour | Close Hour | Phone        | Website     |Drink | Rating |
+======+==============+==========+=======+=======+===========+============+==============+=============+======+========+
| Shop | 124 Some Ave | Portland | OR    | 97006 | 8:00 AM   | 5:00 PM    | 530-123-4567 | milktea.com | Taro | 5      |
+------+--------------+----------+-------+-------+-----------+------------+--------------+-------------+------+--------+

This can be created with the following SQL (see bottom of this file):

    create table shoplist (name text, street text, city text, state text, zip int, open_hr text, close_hr text,
    phone text, website, drink text, rating int);


"""
from datetime import date
from .Model import Model
import sqlite3

DB_FILE = 'shops.db'  # file for our Database


class model(Model):
    """
    Initializing method. Runs a 'COUNT' query to verify if the table exists. If an exception is returned, it creates the table.
    """
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT COUNT(rowid) FROM shoplist")
        except sqlite3.OperationalError:
            cursor.execute("CREATE TABLE shoplist (name text, street text, city text, state text, zip integer, open_hr text, close_hr text, phone text, drink text, rating integer, website text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, street, city, state, zip, open_hr, close_hr, phone, website, drink, rating
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM shoplist")
        except sqlite3.OperationalError:
            cursor.execute("CREATE TABLE shoplist (name text, street text, city text, state text, zip integer, open_hr text, close_hr text, phone text, drink text, rating integer, website text)")
        return cursor.fetchall()

    def insert(self, name, street, city, state, zip, open_hr, close_hr, phone, website, drink, rating):
        """
        Inserts entry into database
        :param name: String
        :param street: String
        :param city: String
        :param state: String
        :param zip: int
        :param open_hr: String
        :param close_hr: String
        :param phone: String
        :param website: String
        :param drink: String
        :param rating: int
        :return: none
        :raises: Database errors on connection and insertion
        """

        params = {'name': name, 'street': street, 'city': city, 'state': state, 'zip': zip, 'open_hr': open_hr,
                  'close_hr': close_hr, 'phone': phone, 'website':website, 'drink': drink, 'rating': rating}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into shoplist (name, street, city, state, zip, open_hr, close_hr, phone, drink, rating, website) "
                       "VALUES (:name, :street, :city, :state, :zip, :open_hr, :close_hr, :phone, :drink, :rating, :website)",
                       params)

        connection.commit()
        cursor.close()
        return True
