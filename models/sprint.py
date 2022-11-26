import peewee

from models.baseModel import BaseModel
from models.task import Task


class Sprint(BaseModel):
    number = peewee.IntegerField()
    data_start = peewee.DateTimeField(null=True)
    data_end = peewee.DateTimeField(null=True)


class SprintTask(BaseModel):
    sprint = peewee.ForeignKeyField(Sprint, backref="sprint")
    task = peewee.ForeignKeyField(Task, backref="sprint")
