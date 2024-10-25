from enum import Enum
from tkinter import Tk, StringVar
from tkinter.ttk import Radiobutton, Frame, Style, Label


class AddEventWindow(Tk):
    def __init__(self, title_: str, size_: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title(title_)
        self.geometry(size_)

        RadBtnsLvlsFrame(self)


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
        self.pack(side='left', anchor='se')
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

        for chs in LvlChooise:
            Radiobutton(
                self, text=f'{chs.value}', 
                variable=val,
                command=lambda: v.config(text=f'Value: {val.get()}'),
                value=chs,
                style='RB.TRadiobutton'
                ).pack(anchor='w')




if __name__ == "__main__":
    add = AddEventWindow(title_='Add event', size_='600x400')
    add.mainloop()