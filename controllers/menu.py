from utils import menus
from views.menu_views import MenuViews
from controllers.backlog_controller import BacklogController
from controllers.sprints_controller import SprintsController


class Menu:
    def __init__(self):
        self.backlog_controller = BacklogController()
        self.sprints_controller = SprintsController()

    def run(self):
        self._main_menu()

    def _main_menu(self):
        user_choice = None
        while user_choice != 2:
            user_choice = MenuViews.display_main_menu(menus.main_menu)
            if user_choice == 0:
                self.backlog_controller.run()
            elif user_choice == 1:
                self.sprints_controller.run()
            else:
                print("Thank you ! Good bye !")
