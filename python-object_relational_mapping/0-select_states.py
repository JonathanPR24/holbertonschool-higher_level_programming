#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Get the MySQL database credentials from command-line arguments
    u_name = argv[1]   # Username
    psw = argv[2]      # Password
    base = argv[3]     # Database name

    # Connecting to the MySQL database
    db = MySQLdb.connect(host="localhost", user=u_name,
            passwd=psw, db=base, port=3306)

    # Creating a cursor object
    cur = db.cursor()

    """Executing MySQL Query to retrieve all states from the
    'states' table ordered by id"""
    cur.execute("SELECT * FROM states ORDER BY id")

    # Obtaining Query Result & printing the result in rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean Up: Closing the cursor and the database connection
    cur.close()
    db.close()
