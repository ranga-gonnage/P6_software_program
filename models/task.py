import datetime
import peewee

from models.baseModel import BaseModel


class Task(BaseModel):
	title = peewee.TextField()
	description = peewee.TextField()
	data_added = peewee.DateField(default=datetime.date.today)
	data_completed = peewee.DateTimeField(null = True)
	status = peewee.TextField()