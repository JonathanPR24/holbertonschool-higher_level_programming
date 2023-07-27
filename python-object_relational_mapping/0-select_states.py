#!/usr/bin/env python3
import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to the MySQL server running on localhost at port 3306
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = conn.cursor()
        
        # Execute the query to fetch all states in ascending order by states.id
        query = "SELECT id, name FROM states ORDER BY id ASC"
        cursor.execute(query)

        # Fetch and display the results
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL server: {e}")
        sys.exit(1)
    finally:
        # Close the database connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    list_states(username, password, database)
