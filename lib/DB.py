# handle connection with db
import mysql.connector
from mysql.connector import errorcode


class DbConn:
    def __init__(self) -> None:
        self.__db_conn = self.__connect_to_db()
        self.__db_cursor = None

    # connect to the db server
    @staticmethod
    def __connect_to_db():
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="password",
                database="hello_python"
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                exit()

    # get db cursor
    def get_cursor(self):
        self.__db_cursor = self.__db_conn.cursor(prepared=True)
        return self.__db_cursor

    def commit(self) -> 'DbConn':
        self.__db_conn.commit()
        return self

    def close_cursor(self) -> 'DbConn':
        self.__db_cursor.close()
        return self

    def close_db_connection(self) -> None:
        self.__db_conn.close()


class Test:
    pass;
