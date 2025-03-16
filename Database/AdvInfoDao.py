from peewee import *
from Database import db

class Advertisement(Model):
    id = AutoField() 
    advnumber = CharField()
    title = TextField()
    description = TextField()
    fraudadv = IntegerField()

    class Meta:
        database = db
        db_table='advertisements' 