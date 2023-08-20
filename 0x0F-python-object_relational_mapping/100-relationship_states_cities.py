#!/usr/bin/python3
"""
 a script that creates the State
 “California” with the City “San Francisco”
 from the database hbtn_0e_100_usa
 """
from sqlalchemy import create_engine
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker


url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
engine = create_engine(url, pool_pre_ping=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_state = State(name='California')
#new_state.name = 'California'
session.add(new_state)
session.commit()

new_city = City()
new_city.name = 'San Francisco'
new_city.state_id = new_state.id
session.add(new_city)

session.commit()
session.close()
