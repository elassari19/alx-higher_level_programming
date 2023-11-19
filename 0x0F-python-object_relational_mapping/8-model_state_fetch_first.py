#!/usr/bin/python3
"""
should prints the first State object
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    sqlEngine = create_engine('mysqluser+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(sqlEngine)
    Session = sessionmaker(bind=sqlEngine)
    session = Session()
    first = session.query(State).order_by(State.id).first()
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    session.close()