import datetime

from utils import menus
from views.menu_views import MenuViews
from views.sprint_views import SprintViews
from models.task import Task
from models.backlog import Backlog
from models.sprint import Sprint, SprintTask


class SprintController:
    def __init__(self, number):
        self.number = number

    def run(self):
        self._menu()

    def _menu(self):
        user_choice = None
        while user_choice != 4:
            user_choice = MenuViews.display_main_menu(menus.sprint_menu)
            if user_choice == 0:
                self._view_sprint()
            elif user_choice == 1:
                self._add_task_from_backlog()
            elif user_choice == 2:
                self._update_task()
            elif user_choice == 3:
                self._delete_task()

    def _view_sprint(self):
        sprint_tasks = SprintTask.select().where(SprintTask.sprint==self._get_sprint())
        tasks = [task.task for task in sprint_tasks]
        SprintViews.print_sprint(tasks)

    def _update_task(self):
        sprint_tasks = SprintTask.select().where(SprintTask.sprint==self._get_sprint())
        tasks = [task.task for task in sprint_tasks]
        task_id_to_update = SprintViews.get_task_to_update(tasks)
        task_to_update = Task.get(Task.id==task_id_to_update)
        task_to_update.title = self._get_text_input("Title of the task")
        task_to_update.description = self._get_text_input("Description of the task")
        task_to_update.data_added = self._get_date_input("Date added")
        task_to_update.data_completed = self._get_date_input("Date completed")
        task_to_update.status = self._get_text_input("Status of the task")
        task_to_update.save()

    def _delete_task(self):
        sprint_tasks = SprintTask.select().where(SprintTask.sprint==self._get_sprint())
        tasks = [task.task for task in sprint_tasks]
        task_id_to_update, task_to_update = SprintViews.get_task_to_update(tasks)
        sprint_tasks = SprintTask.get(SprintTask.task==task_to_update)
        sprint_tasks.delete_instance()
        task = Task.get(Task.id==task_id_to_update)
        task.delete_instance()

    def _add_task_from_backlog(self):
        backlog = Backlog.select()
        task_id_to_add = SprintViews.get_task_from_backlog(backlog)
        task_to_add = Task.get(Task.id==task_id_to_add)
        sprint = SprintTask.create(sprint=self._get_sprint(), task=task_to_add)
        sprint.save()
        backlog_item_to_delete = Backlog.get(Backlog.task == task_id_to_add)
        backlog_item_to_delete.delete_instance()


    def _get_sprint(self):
        return Sprint.get(Sprint.number==self.number)

    def _get_text_input(self, user_question):
        user_input = ""
        while not user_input.isalpha():
            user_input = SprintViews.get_text(user_question)
        return user_input

    def _get_date_input(self, user_question):
        user_input = ""
        while not self._is_date_valid(user_input):
            user_input = SprintViews.get_text(user_question)
        return user_input

    def _is_date_valid(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            return False
        return True
