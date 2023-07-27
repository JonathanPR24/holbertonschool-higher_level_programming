#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

def list_states(username, password, database):
    """
    Lists all states from the specified database.

    Arguments:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

        # Create a cursor to interact with the database
        cursor = db.cursor()

        # Execute the query to select all states ordered by id in ascending order
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the results and print them as shown in the example
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to the database: {e}")
    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database)
