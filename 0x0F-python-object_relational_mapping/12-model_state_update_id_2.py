#!/usr/bin/python3
"""
should changes the name of a State object
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
    state = session.query(State).filter_by(id=2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
