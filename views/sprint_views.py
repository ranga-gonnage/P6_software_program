from rich.console import Console
from rich.table import Table
from simple_term_menu import TerminalMenu


class SprintViews:
    @staticmethod
    def get_text(user_question):
        """
            complexity : O(1)
        """
        user_input = input(f"{user_question} : ")
        return user_input

    @staticmethod
    def print_sprint(tasks):
        """
            complexity : O(n)
        """
        console = Console()

        table = Table(show_header=True, header_style="bold blue")
        table.add_column("Id#", style="dim", width=6)
        table.add_column("Title", min_width=20)
        table.add_column("Description", min_width=12, justify="right")
        table.add_column("data added", min_width=12, justify="right")
        table.add_column("data completed", min_width=12, justify="right")
        table.add_column("status", min_width=12, justify="right")

        for task in tasks:
            table.add_row(
                str(task.id),
                task.title,
                task.description,
                str(task.data_added),
                str(task.data_completed),
                task.status,
            )

        console.print(table)

    @staticmethod
    def get_task_to_update(tasks):
        """
            complexity : O(n)
        """
        items = [f"{index + 1} : {item.title}" for index, item in enumerate(tasks)]
        terminal_menu = TerminalMenu(items, accept_keys=("enter", "alt-d", "ctrl-i"))
        menu_entry_index = terminal_menu.show()
        return tasks[menu_entry_index].id, tasks[menu_entry_index]

    @staticmethod
    def get_task_from_backlog(backlog):
        """
            complexity : O(n)
        """
        items = [
            f"{index + 1} : {item.task.title}" for index, item in enumerate(backlog)
        ]
        terminal_menu = TerminalMenu(items, accept_keys=("enter", "alt-d", "ctrl-i"))
        menu_entry_index = terminal_menu.show()
        return backlog[menu_entry_index].task.id
