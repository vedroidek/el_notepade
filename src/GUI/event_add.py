from enum import Enum
from tkinter import Tk, StringVar, Toplevel
from tkinter.ttk import Radiobutton, Frame, Style, Label, Entry


class AddEventWindow(Toplevel):
    def __init__(self, title_: str, size_x: int, size_y: int,
                  *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title(title_)
        self.geometry(f'{size_x}x{size_y}')

        self.configure_column()

        self.rb_frame()
        self.field_entry_title()

    def configure_column(self, min_size: int=100):
        """
        Minimum grid cell width for a column.
        """
        self.grid_columnconfigure(0, minsize=min_size)
        self.grid_columnconfigure(1, minsize=min_size)

    def field_entry_title(self):
        tv = StringVar()
        et = Entry(self, textvariable=tv)
        et.grid(column=0, row=0, padx=3, pady=3)

    def rb_frame(self):
        """
        Initialize frame radio button.
        """
        rb = RadBtnsLvlsFrame(self)
        rb.grid(column=0, row=3, padx=3, stick='w')
        


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
        # self.pack(side='left', anchor='se')

        self.frame_style()
        self.chooise_lvl()

    def frame_style(self, font: str=None, background: str=None):
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
