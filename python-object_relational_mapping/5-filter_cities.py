#!/usr/bin/python3
"""
Script that lists all cities of a specific state from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

def filter_cities_by_state(username, password, database_name, state_name):
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

        # Use parameterized query to prevent SQL injection
        query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id"
        cursor.execute(query, (state_name,))

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display the results
        cities = [row[0] for row in rows]
        print(", ".join(cities))

    except MySQLdb.Error as e:
        # If there is an error, print the error message
        print("Error:", e)

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()

# Check if the script is run as the main module
if __name__ == "__main__":
    # Check if all four arguments are provided (username, password, database name, state name)
    if len(sys.argv) != 5:
        # Print the usage message and exit with an error code of 1
        print("Usage: python script_name.py <username> <password> <db_name> <state_name>")
        sys.exit(1)

    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to list all cities of the specific state from the database
    filter_cities_by_state(username, password, database_name, state_name)
