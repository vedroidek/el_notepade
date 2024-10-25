from typing import Iterable
from tkinter import Tk, Button
from tkinter.ttk import Label
from event_add import AddEventWindow
from stat_bar import StatusBar


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
        # self.iconbitmap(f'/home/max/python_proj/el_notepade/src/GUI/icon.ico')
        self.title(title_)
        self.geometry(f"{winsize[0]}x{winsize[1]}+100+100") # spaces are not allowed!
        self.resizable(is_resizeble[0], is_resizeble[1])

        self.label = Label(text="My Notes",
                           background='gray35',
                           foreground='dark orange',
                           font=('Helvetica', 10, 'bold'),
                           padding=(10, 6),
                           relief='raised')
        self.label.pack(pady=10, padx=10)

        # BUTTONS #
        btn_exit = Button(
            self, text="Exit", 
            command=self.close,
            padx = 10, pady = 10,
            foreground='red3',
            background='black',
            activebackground='medium blue'
            )
        self.main_btns()

        StatusBar(self)

        btn_exit.pack(pady=10, padx=10, anchor='se', side='bottom')

    # HANDLERS OF BUTTONS
    def new_event(self):
        window = AddEventWindow(
            title_='Add event',
            size_='600x400'
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

    def close(self):
        """ Close main window. """
        return self.quit()
    
    def main_btns(self):
        methods = {
        'add': self.new_event,
        'del': self.del_event,
        'change': self.change_event,
        'show': self.get_event
        }

        for key, val in methods.items():
            Button(self, text=f"{key}", command=val).pack(anchor='w')


if __name__ == "__main__":
    app = Notification(winsize=(800, 400), 
                       title_='El Notepade, Amigo v0.1.0')    
    app.mainloop()
    