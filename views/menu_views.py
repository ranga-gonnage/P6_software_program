from simple_term_menu import TerminalMenu


class MenuViews:
    @staticmethod
    def display_main_menu(items):
        terminal_menu = TerminalMenu(items, accept_keys=("enter", "alt-d", "ctrl-i"))
        menu_entry_index = terminal_menu.show()
        return menu_entry_index
