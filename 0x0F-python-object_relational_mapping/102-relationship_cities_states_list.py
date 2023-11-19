#!/usr/bin/python3

"""
should lists all City objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    sqlEngine = create_engine('mysqluser+mysqldb://{}:{}@localhost/{}'.format
                              (sys.argv[1], sys.argv[2], sys.argv[3]),
                              pool_pre_ping=True)
    Base.metadata.create_all(sqlEngine)
    Session = sessionmaker()
    Session.configure(bind=sqlEngine)
    session = Session()
    rows = session.query(State).all()
    for state in rows:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.close()
