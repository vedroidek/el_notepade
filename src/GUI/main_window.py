from typing import Iterable
from tkinter import Tk, messagebox, Button, Variable, Listbox
from tkinter.ttk import Label, Frame
from GUI.event_add import AddEventWindow
from GUI.stat_bar import StatusBar


class Notification(Tk):
    """
    Initialize the creation of the main window.
    Params:
        : winsize : iterable sequence of two integers 'winsize=(600, 400)'
            window size in pixels along the X and Y axes
        : title : str - variable length string 'title=\"My app\"'. Will appear as a title
            on the main window.
        : is_resizeble : iterable sequence of two bool 'resizable=(False, False)'
            whether to allow window resizing along the X and Y axes
            default: False X, False Y
    """

    def __init__(
            self,
            winsize: Iterable[int],
            title_: str,
            is_resizeble: Iterable[bool] = (False, False),
            *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.title(title_)
        
        self.geometry(f"{winsize[0]}x{winsize[1]}+100+100") # spaces are not allowed!
        self.minsize(800, 400)
        self.resizable(is_resizeble[0], is_resizeble[1])

        StatusBar(self)
        MainButtonsFrame(self)
        EventDisplayFrame(self)

        self.name_app()
        self.quit_btn()

    def name_app(self, name: str = None):
        """ 
        Installation and placement 
        of a name plate in the main window. 
        :param :name (str)
        """
        self.label = Label(text=name or "My Notes",
                           background='gray35',
                           foreground='dark orange',
                           font=('Helvetica', 10, 'bold'),
                           padding=(10, 6),
                           relief='raised')
        self.label.place(relx=0.5, anchor='n', relwidth=0.2)

    # # HANDLERS OF BUTTONS
    # def new_event(self):
    #     """
    #     Open a new window to add an event.
    #     """
    #     window = AddEventWindow(
    #         title_='Add event',
    #         size_x=600,
    #         size_y=400
    #     )

    # def get_event(self):
    #     """ Show event. """
    #     pass

    # def change_event(self):
    #     """ Change event if already exists. """
    #     window = Tk()
    #     window.title("Change event")
    #     window.geometry("400x300")

    # def del_event(self):
    #     """ Delete event. """
    #     window = Tk()
    #     window.title("Delete event")
    #     window.geometry("400x300")

    def quit_btn(self):
        """
        Button for close to application.
        """
        btn_exit = Button(
            self, text="Exit",
            command=lambda: self.check(title='Quit', message='Are you sure?'),
            padx=10, pady=10,
            foreground='red3',
            background='black',
            activebackground='medium blue'
        )
        btn_exit.place(relx=0.93, rely=0.83)

    def check(self, title: str, message: str):
        """ Close main window. """
        answer = messagebox.askyesno(title=title, message=message)
        if answer:
            self.quit()


class MainButtonsFrame(Frame):
    """
    Frame for placing the main buttons on the main widget.
    """
    def __init__(self, master: 'Tk'):
        super().__init__(
            master=master,
            relief='flat')
        self.place(anchor='w', rely=0.45)

        self.main_btns()

    def main_btns(self):
        """
        Creating main buttons for working with events.
        """
        methods = {
            'add': {'name': self.new_event, 'color': 'green'},
            'show': {'name': self.get_event, 'color': 'yellow'},
            'change': {'name': self.change_event, 'color': 'yellow'},
            'del': {'name': self.del_event, 'color': 'red'},
        }

        for btn_name, event in methods.items():
            Button(self, text=f"{btn_name}",
                   background=event['color'],
                   command=event['name'], height=2,
                   width=10).pack()
            
    # HANDLERS OF BUTTONS
    def new_event(self):
        """
        Open a new window to add an event.
        """
        window = AddEventWindow(
            title_='Add event',
            size_x=600,
            size_y=400
        )

    def get_event(self):
        """ Show event. """
        pass

    def change_event(self):
        """ Change event if already exists. """
        window = Tk()
        window.title("Change event")
        window.geometry("400x300")

    def del_event(self):
        """ Delete event. """
        window = Tk()
        window.title("Delete event")
        window.geometry("400x300")


class EventDisplayFrame(Frame):
    """
    Widget for displaying saved events.
    """
    def __init__(self, master: 'Tk'):
        super().__init__(
            master=master,
            relief='sunken'
        )
        self.place(relx=0.2, rely=0.2, relheight=0.5, relwidth=0.5)

        self.events_listbox(events=[f'{2**i}' for i in range(40)]) # THIS SAMPLE EXAMPLE

    def events_listbox(self, events: Iterable[str]):
        """
        Box of display all events.
        """
        languages_var = Variable(value=events)
        languages_listbox = Listbox(self, listvariable=languages_var)
        languages_listbox.pack(expand=1, fill='both')
