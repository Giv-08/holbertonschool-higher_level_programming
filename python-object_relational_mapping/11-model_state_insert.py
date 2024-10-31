#!/usr/bin/python3
""" This module is for adding the State object “Louisiana”
to the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
        )

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)

    session.close()
