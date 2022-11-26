import peewee
from models.baseModel import BaseModel
from models.task import Task

class Backlog(BaseModel):
	task = peewee.ForeignKeyField(Task, backref='backlog')

