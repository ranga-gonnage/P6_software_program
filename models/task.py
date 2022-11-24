import datetime
import peewee

from baseModel import BaseModel


class Task(BaseModel):
	title = peewee.TextField()
	description = peewee.TextField()
	data_added = peewee.DateTimeField(default=datetime.datetime.now)
	data_completed = peewee.DateTimeField()
	status = peewee.TextField()