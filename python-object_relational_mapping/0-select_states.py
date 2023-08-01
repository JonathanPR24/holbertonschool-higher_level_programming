#!/usr/bin/python3

""" Import necessary libraries """
import sys
import MySQLdb

def list_states(username, password, database_name):
    """ 
    Connect to the MySQL server and list all states from the 'states' table.

    Parameters:
        username (str): The MySQL server username.
        password (str): The MySQL server password.
        database_name (str): The name of the database containing the 'states' table.
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database_name,
        port=3306
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    try:
        # Execute the SQL query to retrieve all states from the 'states' table in ascending order by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except Exception as e:
        # If there is an error, print the error message
        print("Error:", e)

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()


# Check if the script is run as the main module
if __name__ == "__main__":
    # Check if all three arguments are provided (username, password, database name)
    if len(sys.argv) != 4:
        # Print the usage message and exit with an error code of 1
        print("Usage: python script_name.py <username> <password> <db_name>")
        sys.exit(1)

    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Call the main function to list states from the database
    list_states(username, password, database_name)
