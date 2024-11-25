from tkinter import Toplevel, Label, Button, messagebox

# from GUI.event_add import AddEventWindow
# from DB.init_db import EventManager


class ChangeEventWindow(Toplevel):  # Подучить наследование
    def __init__(self, title_: str, size_x: int, size_y: int,
                 *args, **kwargs) -> None:
        super().__init__()

        self.title(title_)
        self.geometry(f'{size_x}x{size_y}')
        self.minsize(width=600, height=400)

        self.configure_column(columns=1, min_size=200)
        self.configure_row()

        self.window_choose_event()
        self.create_buttons()

    def configure_column(self, columns: int, min_size: int = 100):
        """
        Minimum grid cell width for a column.
        """
        for col_num in range(columns):
            self.grid_columnconfigure(col_num, minsize=min_size)

    def configure_row(self):
        self.grid_rowconfigure(index=1, minsize=20)
        self.grid_rowconfigure(index=2, minsize=100)

    def window_choose_event(self):  # Очень сыро. Доделать
        # events = show_all_events()
        events = [(1, 'дерево', '11', 1111), (2, 'куст', '22', 2222), (3, 'трава', '33', 3333)]

        for idx, title, _, _ in events:
            event_label = Label(self, text=title)
            event_label.grid(column=0, row=idx - 1, sticky='w', padx=20)

    def create_buttons(self):  # Очень сыро. Доделать
        change_button = Button(self, text="Choose", command=...)
        change_button.grid(column=1,row=4, padx=5, pady=5)

        exit_button = Button(self, text="Exit", command=self.confirm_exit)
        exit_button.grid(column=1, row=5, padx=5, pady=5)

    def confirm_exit(self):
        """
        Confirm exit window
        """
        if messagebox.askyesno("Confirmation of the exit", "Do you really want to get out?"):
            self.destroy()

    def window_change_event(self):
        pass