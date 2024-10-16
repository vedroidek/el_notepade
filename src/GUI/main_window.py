from typing import Iterable
from tkinter import Tk, Button, Label
from events import AddEventWindow
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
                           fg='dark orange',
                           font=('Helvetica', 10, 'bold'),
                           padx=10, pady=6,
                           relief='raised')
        self.label.pack(pady=10, padx=10)

        # BUTTONS #
        btn_exit = Button(
            self, text="Exit", 
            command=self.close,
            padx=10,
            pady=10,
            fg='red3',
            background='black',
            activebackground='medium blue'
            )
        btn_add = Button(self, text="Add", command=self.new_event)
        btn_del = Button(self, text="Del", command=self.del_event)
        btn_change = Button(self, text="Change", command=self.change_event)
        btn_get = Button(self, text="Show", command=self.get_event)
        
        btn_get.pack(anchor='w')
        btn_del.pack(anchor='w')
        btn_change.pack(anchor='w')
        btn_add.pack(anchor='w')

        StatusBar(self)

        btn_exit.pack(pady=10, padx=10, anchor='se', side='bottom')

    # HANDLERS OF BUTTONS
    def new_event(self):
        window = AddEventWindow(
            title_='Add event',
            size_='400x400'
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


if __name__ == "__main__":
    app = Notification(winsize=(800, 400), 
                       title_='El Notepade, Amigo')    
    app.mainloop()
    