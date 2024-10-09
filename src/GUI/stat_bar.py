from tkinter import Frame, Label
from datetime import datetime


class StatusBar(Frame):
    def __init__(self, parent: 'Tk'):
        Frame.__init__(self, parent)

        statusbar = Label(parent, 
                          background='black',
                          fg='yellow',
                          relief = 'sunken', anchor = 'w',
                          text=f'{datetime.now().strftime("%d/%M/%Y")}')
        statusbar.pack(anchor='s', side = 'bottom', fill = 'x')
