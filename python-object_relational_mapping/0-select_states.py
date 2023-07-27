#!/usr/bin/python3

import sys
import MySQLdb

def list_states(username, password, database_name):
    try:
        # Connect to the MySQL server using a context manager
        with MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database_name,
            port=3306
        ) as db:

            # Create a cursor using a context manager
            with db.cursor() as cursor:
                # Execute the SQL query to retrieve all states from the table
                # in ascending order by id
                cursor.execute("SELECT * FROM states ORDER BY id ASC")

                # Fetch all rows from the result set
                rows = cursor.fetchall()

                # Display the results
                for row in rows:
                    print(row)

    except MySQLdb.Error as e:
        # If there is an error, print the error message
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <username> <password> <db_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    list_states(username, password, database_name)
