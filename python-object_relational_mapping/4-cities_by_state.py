#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

def list_cities(username, password, database_name):
    try:
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

        # Execute the SQL query to retrieve all cities with corresponding state names
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                 JOIN states ON cities.state_id = states.id ORDER BY cities.id"
        cursor.execute(query)

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
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

    # Call the function to list all cities from the database
    list_cities(username, password, database_name)
