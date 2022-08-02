from sqlalchemy import create_engine, MetaData
import postgresql

# Hay que crear la base de datos primero

SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:eemcdps@localhost:5432/storedb'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

meta = MetaData()

conn = engine.connect()