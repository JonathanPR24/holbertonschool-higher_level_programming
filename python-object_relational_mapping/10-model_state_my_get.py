#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

    # Create the engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the State object with the specified name
    state = session.query(State).filter_by(name=state_name).first()

    # Display the result
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
