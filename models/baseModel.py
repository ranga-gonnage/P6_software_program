import peewee

db = peewee.SqliteDatabase("database.sqlite3")


class BaseModel(peewee.Model):
    class Meta:
        database = db
