#!/usr/bin/python3
"""
should improve the files model_city.py and model_state.py, and save them as relationship_city.py and relationship_state.py
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
    Session = sessionmaker(bind=sqlEngine)
    session = Session()
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
    session.close()
