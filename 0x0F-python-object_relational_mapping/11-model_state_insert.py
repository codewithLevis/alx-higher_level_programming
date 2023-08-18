#!/usr/bin/python3
"""
script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""
from sqlalchemy import insert, create_engine
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    uri = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(uri, pool_pre_ping=True)
    conn = engine.connect()
    query = insert(State).values(name='Louisiana')
    result = conn.execute(query)
    print(result.inserted_primary_key[0])
    conn.close()
