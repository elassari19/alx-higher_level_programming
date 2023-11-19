#!/usr/bin/python3
"""
should defini a class of a City
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    sqlEngine = create_engine('mysqluser+mysqldb://{}:{}@localhost/{}'.format
                              (sys.argv[1], sys.argv[2], sys.argv[3]),
                              pool_pre_ping=True)
    Base.metadata.create_all(sqlEngine)
    Session = sessionmaker(bind=sqlEngine)
    session = Session()
    rows = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for city, state in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
