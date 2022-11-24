import peewee
from baseModel import BaseModel
from task import Task

class Backlog(BaseModel):
	task = peewee.ForeignKeyField(Task, backref='backlog')

