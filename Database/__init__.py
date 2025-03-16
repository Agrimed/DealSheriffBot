from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from peewee import *

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)

db = PostgresqlDatabase(
    'test',
    user='postgres',
    password='password',
    host='localhost',
    port=5432
)