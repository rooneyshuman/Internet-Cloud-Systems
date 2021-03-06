"""
Abstract data model class that serves as the base class for specific model instantiations
"""
class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, name, street, city, state, zip, open_hr, close_hr, phone, website, drink, rating):
        """
        Inserts entry into database
        :param name: String
        :param street: String
        :param city: String
        :param state: String
        :param zip: integer
        :param open_hr: String
        :param close_hr: String
        :param phone: String
        :param website: String
        :param drink: String
        :param rating: integer
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass

    def delete(self, name):
        """
        Deletes an entry from the database
        :param name: String
        :return: none
        :raises: Database errors on connection and deletion
        """
        pass
