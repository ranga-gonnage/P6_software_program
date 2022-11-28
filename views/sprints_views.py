from rich.console import Console
from rich.table import Table
from simple_term_menu import TerminalMenu


class SprintsViews:
    @staticmethod
    def get_text(user_question):
        user_input = input(f"{user_question} : ")
        return user_input

    @staticmethod
    def print_sprints(sprints):
        """
            complexity : O(n)
        """
        console = Console()

        table = Table(show_header=True, header_style="bold blue")
        table.add_column("Id#", style="dim", width=6)
        table.add_column("Number", min_width=20)
        table.add_column("Date start", min_width=12, justify="right")
        table.add_column("Date end", min_width=12, justify="right")

        for item in sprints:
            table.add_row(
                str(item.id), str(item.number), str(item.data_start), str(item.data_end)
            )

        console.print(table)

    @staticmethod
    def get_sprints_to_update(sprints):
        """
            complexity : O(n)
        """
        items = [f"{index + 1} : {item.number}" for index, item in enumerate(sprints)]
        terminal_menu = TerminalMenu(items, accept_keys=("enter", "alt-d", "ctrl-i"))
        menu_entry_index = terminal_menu.show()
        return sprints[menu_entry_index].id
