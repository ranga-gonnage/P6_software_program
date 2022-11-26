import datetime

from utils import menus
from views.menu_views import MenuViews
from views.backlog_views import BacklogViews
from models.task import Task
from models.backlog import Backlog


class BacklogController:
    def run(self):
        self._menu()

    def _menu(self):
        user_choice = None
        while user_choice != 4:
            user_choice = MenuViews.display_main_menu(menus.backlog_menu)
            if user_choice == 0:
                self._view_backlog()
            elif user_choice == 1:
                self._create_task()
            elif user_choice == 2:
                self._update_task()
            elif user_choice == 3:
                self._delete_task()

    def _view_backlog(self):
        backlog = Backlog.select()
        BacklogViews.print_backlog(backlog)

    def _create_task(self):
        title = self._get_text_input("Title of the task")
        description = self._get_text_input("Description of the task")
        status = self._get_text_input("Status of the task")
        task = Task.create(title=title, description=description, status=status)
        task.save()
        backlog = Backlog.create(task=task)
        backlog.save()

    def _update_task(self):
        backlog = Backlog.select()
        task_id_to_update = BacklogViews.get_task_to_update(backlog)
        task_to_update = Task.get(Task.id==task_id_to_update)
        task_to_update.title = self._get_text_input("Title of the task")
        task_to_update.description = self._get_text_input("Description of the task")
        task_to_update.data_added = self._get_date_input("Date added")
        task_to_update.data_completed = self._get_date_input("Date completed")
        task_to_update.status = self._get_text_input("Status of the task")
        task_to_update.save()

    def _delete_task(self):
        backlog = Backlog.select()
        task_id_to_update = BacklogViews.get_task_to_update(backlog)
        backlog_item_to_delete = Backlog.get(Backlog.task == task_id_to_update)
        backlog_item_to_delete.delete_instance()
        task_to_delete = Task.get(Task.id == task_id_to_update)
        task_to_delete.delete_instance()

    def _get_text_input(self, user_question):
        user_input = ""
        while not user_input.isalpha():
            user_input = BacklogViews.get_text(user_question)
        return user_input

    def _get_date_input(self, user_question):
        user_input = ""
        while not self._is_date_valid(user_input):
            user_input = BacklogViews.get_text(user_question)
        return user_input

    def _is_date_valid(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            return False
        return True




