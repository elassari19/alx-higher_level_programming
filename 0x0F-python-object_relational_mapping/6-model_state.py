#!/usr/bin/python3
"""
should defin State instance Base = declarative_base()
"""

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    sqlEngine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(sqlEngine)
