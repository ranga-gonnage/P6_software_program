from models.task import Task
from models.backlog import Backlog
from models.sprint import Sprint, SprintTask

if __name__ == "__main__":
    Task.create_table()
    Backlog.create_table()
    Sprint.create_table()
    SprintTask.create_table()
