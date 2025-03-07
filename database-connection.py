import mysql.connector
import constants
import queries



class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=constants._DB_HOST,
            user=constants._DB_USER,
            password=constants._DB_PASSWORD,  # na2s check  complex password
            database= constants._DB_NAME # da name bta3 el Table
        )
        self.cursor = self.conn.cursor()  # create cursor to excute instructions

    # this functions to excute table's functions
    # query -->insert update delete select
    # params---> the data will give with table's functions

    # def execute(self, query, params=None):  # to excute INSERT, UPDATE, DELETE
    #     self.cursor.execute(query, params or ())
    #     self.conn.commit()  # commit to save changes
    #
    # def fetchall(self, query, params=None):  # to excute SELECT
    #     self.cursor.execute(query, params or ())
    #     return self.cursor.fetchall()
    #
    # def fetchone(self, query, params=None):  # to get only one row
    #     self.cursor.execute(query, params or ())
    #     return self.cursor.fetchone()

    def close(self):  # the connection should be closed after excute
        self.conn.close()
