#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

# connect to mysql
try:
    dbConn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="hello_python"
    )

    dbCursor = dbConn.cursor(prepared=True)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
        exit()

sql = """ INSERT INTO student
            (name, address_line_1, address_line_2, postcode, when_created)
            VALUES
            (%s, %s, %s, %s, %s)"""

# open and read the file line by line
lines = open("student.txt", "r")

for line in lines:
    line = line.strip()
    line = line.strip("|")
    lineData = line.split('|')
    name = lineData[0]
    addressLine1 = lineData[1]
    addressLine2 = lineData[2]
    postCode = lineData[3]
    print(name + ' - ' + addressLine1 + ' - ' + addressLine2 + ' - ' + postCode + ' - ' + str(datetime.now()))

    sqlValue = (name, addressLine1, addressLine2, postCode, datetime.now())
    dbCursor.execute(sql, sqlValue)

dbCursor.close()
dbConn.commit()
dbConn.close()