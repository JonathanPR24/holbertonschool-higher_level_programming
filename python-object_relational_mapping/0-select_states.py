#!/usr/bin/python3

import sys
import mysql.connector

def list_states(username, password, database_name):
    try:
        # Connect to the MySQL server
        db = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database=database_name,
            port=3306
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to retrieve all states from the table in ascending order by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except mysql.connector.Error as e:
        # If there is an error, print the error message
        print("Error:", e)

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    # Check if all three arguments are provided (username, password, database name)
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <username> <password> <db_name>")
        sys.exit(1)

    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Call the main function to list states from the database
    list_states(username, password, database_name)
