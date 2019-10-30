"""
Flask app to store and retrieve a list of bubble tea shops
Data is stored in a SQLite database that looks something like the following:

+------------+------------------+------------+-------+-------+-----------+------------+--------------+------------+---------+
| Name       | Address          | City       | State | Zip   | Open Hour | Close Hour | Phone        | Drink      | Rating  |
+============+==================+============+=======+=======+===========+============+==============+============+=========+
| Milk+T     | 1234 Street Ave  | Portland   | OR    | 97006 | 8 AM      | 5 PM       | 530-123-4567 | Milk Tea   | 5       |
+------------+------------------+------------+-------+-------+-----------+------------+--------------+------------+---------+

This can be created with the following SQL (see bottom of this file):

    create table shoplist (name text, street text, city text, state text, zip int, open_hr text, close_hr text,
    phone text, drink text, rating int);


"""
from datetime import date
from .Model import Model
import sqlite3

DB_FILE = 'entries.db'  # file for our Database


class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from shoplist")
        except sqlite3.OperationalError:
            cursor.execute("create table shoplist (name text, street text, city text, state text, zip integer, open_hr text, close_hr text, phone text, drink text, rating integer)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, street, city, state, zip, open_hr, close_hr, phone, drink, rating
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM shoplist")
        return cursor.fetchall()

    def insert(self, name, street, city, state, zip, open_hr, close_hr, phone, drink, rating):
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
        :param drink: String
        :param rating: int
        :return: none
        :raises: Database errors on connection and insertion
        """

        params = {'name': name, 'street': street, 'city': city, 'state': state, 'zip': zip, 'open_hr': open_hr,
                  'close_hr': close_hr, 'phone': phone, 'drink': drink, 'rating': rating}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into shoplist (name, street, city, state, zip, open_hr, close_hr, phone, drink, rating) "
                       "VALUES (:name, :street, :city, :state, :zip, :open_hr, :close_hr, :phone, :drink, :rating)",
                       params)

        connection.commit()
        cursor.close()
        return True
