from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2


engine = create_engine('postgresql://codingbee:bee123@localhost:5432/alchemy', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Bee(Base):
    __tablename__ = 'bee'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    size = Column(Integer)
    bee_type = Column(String(50))


Base.metadata.create_all(engine)