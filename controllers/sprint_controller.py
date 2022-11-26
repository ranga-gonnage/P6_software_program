from utils import menus
from views.menu_views import MenuViews
from views.sprint_views import SprintViews
from models.task import Task
from models.backlog import Backlog


class SprintController:
    def __init__(self, number):
        self.number = number

    def run(self):
        self._menu()

    def _menu(self):
        user_choice = None
        while user_choice != 5:
            user_choice = MenuViews.display_main_menu(menus.sprint_menu)
            if user_choice == 0:
                print("View sprint")
            elif user_choice == 1:
                self._add_task_from_backlog()
            elif user_choice == 2:
                print("Update task")

    def _add_task_from_backlog(self):
        