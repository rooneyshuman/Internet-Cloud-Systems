class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

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
        pass
