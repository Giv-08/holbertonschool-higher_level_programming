#!/usr/bin/python3
# """ This module is a state model class"""
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, create_engine
# import sys

# Base = declarative_base()

# class State(Base):
#     """State class that represents the 'states' table in the database."""
#     __tablename__ = 'states'
#     id = Column(Integer, primary_key=True, unique=True, autoincrement=True ,nullable=False)
#     name = Column(String(128), nullable=False)

# if __name__ == "__main__":
#     # Retrieve MySQL credentials from the command-line arguments
#     username = sys.argv[1]
#     password = sys.argv[2]
#     database = sys.argv[3]

#     # Create the connection URL for MySQL
#     db_url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'

#     # Create a new SQLAlchemy engine instance
#     engine = create_engine(db_url, pool_pre_ping=True)

#     # Create all tables in the database (if they don't already exist)
#     Base.metadata.create_all(engine)
#!/usr/bin/python3
"""
Defines a State class and connects to a MySQL database.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

# Initialize the base class for declarative class definitions
Base = declarative_base()

class State(Base):
    """State class that represents the 'states' table in the database."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
