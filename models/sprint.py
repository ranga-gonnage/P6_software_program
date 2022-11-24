import peewee

from baseModel import BaseModel
from task import Task

class Sprint(BaseModel):
	number = peewee.IntegerField()
	data_start = peewee.DateTimeField()
	data_end = peewee.DateTimeField()
	task = peewee.ForeignKeyField(Task, backref='sprint')