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
            is_resizeble: Iterable[bool]=(False, False),
            *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title(title_)
        self.geometry(f"{winsize[0]}x{winsize[1]}+100+100") # spaces are not allowed!
        self.minsize(800, 400)
        self.resizable(is_resizeble[0], is_resizeble[1])

        StatusBar(self)

        self.name_app()
        EventDisplayFrame(self).pack()

        # BUTTONS #
        self.quit_btn()        
        self.main_btns()

    def name_app(self, name: str=None):
        self.label = Label(text=name or "My Notes",
                           background='gray35',
                           foreground='dark orange',
                           font=('Helvetica', 10, 'bold'),
                           padding=(10, 6),
                           relief='raised')
        self.label.pack(pady=10, padx=10)

        StatusBar(self)

        # BUTTONS #
        self.quit_btn()        
        self.main_btns()

    # HANDLERS OF BUTTONS
    def new_event(self):
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

    def quit_btn(self):
        btn_exit = Button(
            self, text="Exit", 
            command=lambda: self.check(title='Quit', message='Are you sure?'),
            padx = 10, pady = 10,
            foreground='red3',
            background='black',
            activebackground='medium blue'
            )
        btn_exit.pack(pady=10, padx=10, anchor='se', side='bottom')

    def check(self, title :str, message: str):
        """ Close main window. """        
        answer = messagebox.askyesno(title=title, message=message)
        if answer:
            self.quit()
    
    def main_btns(self):
        methods = {
        'add': self.new_event,
        'del': self.del_event,
        'change': self.change_event,
        'show': self.get_event
        }

        for key, val in methods.items():
            Button(self, text=f"{key}", command=val, height=2, width=10).pack(anchor='w')


class EventDisplayFrame(Frame):
    def __init__(self, master: 'Tk'):
        super().__init__(master=master,
                         width=20, height=20,
                         borderwidth=1,
                         relief='sunken')
        
        
    def events_listbox(self, events: Iterable[str]):
        languages = ["Python", "JavaScript", "C#", "Java"]
        languages_var = Variable(value=languages)        
        languages_listbox = Listbox(listvariable=languages_var)        
        languages_listbox.pack()

    