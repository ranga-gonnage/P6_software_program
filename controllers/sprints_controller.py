import datetime

from utils import menus
from views.menu_views import MenuViews
from views.sprints_views import SprintsViews
from models.sprint import Sprint
from controllers.sprint_controller import SprintController


class SprintsController:
    def run(self):
        self._menu()

    def _menu(self):
        """
            complexity : O(1)
        """
        user_choice = None
        while user_choice != 5:
            user_choice = MenuViews.display_main_menu(menus.sprints_menu)
            if user_choice == 0:
                self._view_sprints()
            elif user_choice == 1:
                self._run_sprint_controller()
            elif user_choice == 2:
                self._create_sprint()
            elif user_choice == 3:
                self._update_sprint()
            elif user_choice == 4:
                self._delete_sprint()

    def _view_sprints(self):
        """
            complexity : O(1)
        """
        sprints = Sprint.select()
        SprintsViews.print_sprints(sprints)

    def _create_sprint(self):
        """
            complexity : O(1)
        """
        number = self._get_number_input("Number")
        data_start = self._get_date_input("Date start")
        data_end = self._get_date_input("Date end")
        sprint = Sprint.create(number=number, data_start=data_start, data_end=data_end)
        sprint.save()

    def _update_sprint(self):
        """
            complexity : O(n)
        """
        sprints = Sprint.select()
        sprint_id_to_update = SprintsViews.get_sprints_to_update(sprints)
        sprint_to_update = Sprint.get(Sprint.id == sprint_id_to_update)
        sprint_to_update.number = self._get_number_input("Number")
        sprint_to_update.data_start = self._get_date_input("Date start")
        sprint_to_update.data_end = self._get_date_input("Date end")
        sprint_to_update.save()

    def _delete_sprint(self):
        """
            complexity : O(n)
        """
        sprints = Sprint.select()
        sprint_id_to_update = SprintsViews.get_sprints_to_update(sprints)
        sprint_to_update = Sprint.get(Sprint.id == sprint_id_to_update)
        sprint_to_update.delete_instance()

    def _run_sprint_controller(self):
        """
            complexity : O(1)
        """
        number = self._select_sprint()
        sprint_controller = SprintController(number)
        sprint_controller.run()

    def _select_sprint(self):
        """
            complexity : O(n)
        """
        sprints = Sprint.select()
        sprint_id_to_update = SprintsViews.get_sprints_to_update(sprints)
        sprint_to_update = Sprint.get(Sprint.id == sprint_id_to_update)
        return sprint_to_update.number

    def _get_number_input(self, user_question):
        """
            complexity : O(n)
            n the number of wrong user typing
        """
        user_input = ""
        while not user_input.isnumeric():
            user_input = SprintsViews.get_text(user_question)
        return user_input

    def _get_date_input(self, user_question):
        """
            complexity : O(n)
            n the number of wrong user typing
        """
        user_input = ""
        while not self._is_date_valid(user_input):
            user_input = SprintsViews.get_text(user_question)
        return user_input

    def _is_date_valid(self, date_text):
        """
            complexity : O(1)
        """
        try:
            datetime.datetime.strptime(date_text, "%Y-%m-%d")
        except ValueError:
            return False
        return True
