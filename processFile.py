#!/usr/bin/python3
from lib import DB
from datetime import datetime
db_conn = DB.DbConn()

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
    print('Saving: ' + name)

    sqlValue = (name, addressLine1, addressLine2, postCode, datetime.now())
    db_conn.get_cursor().execute(sql, sqlValue)

db_conn.commit().close_cursor().close_db_connection()
