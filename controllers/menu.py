from utils import menus
from views.menu_views import MenuViews

class Menu:
    def run(self):
        self._main_menu()
        
    def _main_menu(self):
        user_choice = MenuViews.display_main_menu(menus.main_menu)
        while user_choice != 2:
            user_choice = MenuViews.display_main_menu(menus.main_menu)
            if user_choice == 0:
                print("backlog")
            elif user_choice == 1:
                print("sprint") 
            else:
                print("exit")


