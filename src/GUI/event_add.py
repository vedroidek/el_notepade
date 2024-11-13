from enum import Enum
from typing import Optional
from tkinter import Tk, StringVar, Toplevel, messagebox, Entry
from tkinter.ttk import Radiobutton, Frame, Style, Label, Button
from tkcalendar import DateEntry
# from DB.init_db import EventManager


class AddEventWindow(Toplevel):
    def __init__(self, title_: str, size_x: int, size_y: int,
                 *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.title(title_)
        self.geometry(f'{size_x}x{size_y}')
        self.minsize(width=600, height=400)

        self.configure_column(columns=4, min_size=200)
        self.configure_row()

        self.title_label()
        self.field_entry_title()
        self.field_entry_description()
        self.field_entry_date()
        self.field_entry_time()
        self.rb_frame()
        self.create_buttons()

    def title_label(self, headers: Optional[tuple[str]] = None):
        """
        The headers of the input fields
        """
        headers = ("Title of event", 'Description', 'Date')
        for idx, title in enumerate(headers):
            elem = Label(self, text=title)
            elem.grid(column=idx, row=0, sticky='w', padx=20)
        time_label = Label(self, text="Time")
        time_label.grid(column=2, row=2, sticky='w', padx=3)

    def configure_column(self, columns: int, min_size: int = 100):
        """
        Minimum grid cell width for a column.
        """
        for col_num in range(columns):
            self.grid_columnconfigure(col_num, minsize=min_size)

    def configure_row(self):
        self.grid_rowconfigure(index=1, minsize=20)
        self.grid_rowconfigure(index=2, minsize=100)

    def field_entry_title(self):
        """
        Event name input field
        """
        self.title_var = StringVar()
        et = Entry(self, textvariable=self.title_var)
        et.grid(column=0, row=1, padx=3, pady=3)

    def field_entry_description(self):
        """
        Description input field
        """
        self.description_var = StringVar()
        ed = Entry(self, textvariable=self.description_var)
        ed.grid(column=1, row=1, rowspan=3, sticky='ns')

    def field_entry_date(self):
        """
        Date input field
        """
        self.date_var = StringVar()
        date_entry = DateEntry(self, textvariable=self.date_var)
        date_entry.grid(column=2, row=1, padx=3, pady=3)

    def field_entry_time(self):
        """
        Time input field
        """
        self.time_var = StringVar()
        time_entry = Entry(self, textvariable=self.time_var)
        time_entry.grid(column=2, row=2, padx=30, pady=3)
        time_entry.insert(0, "HH:MM")

    def rb_frame(self):
        """
        Initialize frame radio button.
        """
        rb = RadBtnsLvlsFrame(
            self)  # Expected type 'Tk', got 'AddEventWindow' instead
        rb.grid(column=0, row=3, padx=3, ipady=5, stick='w')

    def create_buttons(self):
        """
        Create save, clear all, clear and exit buttons
        """
        save_button = Button(self, text="Save", command=self.save_event)
        save_button.grid(column=0, row=5, padx=5, pady=5)

        clear_button = Button(self, text="Clear everything",
                              command=self.clear_fields)
        clear_button.grid(column=1, row=5, padx=5, pady=5)

        exit_button = Button(self, text="Exit", command=self.confirm_exit)
        exit_button.grid(column=2, row=5, padx=5, pady=5)

        clear_button_disc = Button(self, text="Clear", command=self.clear)
        clear_button_disc.grid(column=1, row=4, padx=5, pady=5)

    def save_event(self):
        """
        Save event in DB. In process...
        """
        title = self.title_var.get()
        description = self.description_var.get()
        date = self.date_var.get()
        time = self.time_var.get()

        if not title or not description or not date or not time:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        # event_manager = EventManager('my_database')
        # event_manager.create_event(title, description, date, time)
        # events = event_manager.get_events()
        # event_manager.close()

    def clear(self):
        """
        Clean description field
        """
        self.description_var.set("")

    def clear_fields(self):
        """
        Clean all input fields
        """
        self.title_var.set("")
        self.description_var.set("")
        self.date_var.set("")
        self.time_var.set("HH:MM")

    def confirm_exit(self):
        """
        Confirm exit window
        """
        if messagebox.askyesno("Confirmation of the exit", "Do you really want to get out?"):
            self.destroy()


class LvlChooise(Enum):
    HIGH: str = 'high'
    MEDIUM: str = 'medium'
    LOW: str = 'low'


class RadBtnsLvlsFrame(Frame):
    """
    An additional frame for placing buttons 
    for selecting the level of event importance.

    params : master - parent vidget, must be type of 'tkinter.Tk'
    """

    def __init__(self, master: 'Tk'):
        super().__init__(
            master,
            borderwidth=2,
            relief='sunken',
            padding=[10, 10, 20, 10],
            style='RB.TFrame',
        )

        self.frame_style()
        self.chooise_lvl()

    def frame_style(self, font: str = None, background: str = None):
        """ Set background of frame using by `Style`. """
        s = Style()
        s.configure(f'RB.{self.winfo_class()}',
                    background='tan2',
                    foreground="#004D40")

    def chooise_lvl(self):
        label_style = Style()
        label_style.configure('RB.TRadiobutton',
                              font="system",
                              background='tan2')

        val = StringVar()
        v = Label(self, text='Value: ')
        v.pack(side='bottom')

        for chs in LvlChooise:
            Radiobutton(
                self, text=f'{chs.value}',
                variable=val,
                command=lambda: v.config(text=f'{val.get().rsplit(".")[-1]}'),
                value=chs,
                style='RB.TRadiobutton'
            ).pack(anchor='w')
