from task import Task
from backlog import Backlog
from sprint import Sprint

if __name__ == '__main__':
	Task.create_table()
	Backlog.create_table()
	Sprint.create_table()