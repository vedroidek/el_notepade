import time
from typing import Optional
from datetime import datetime
from threading import Thread
from tkinter import Frame, Label, StringVar


class StatusBar(Frame):
    """
    Displays the current date and time. in the status bar.
    """

    def __init__(self, master, additional_event: Optional[str] = None):
        Frame.__init__(self, master)
        self.additional_event = additional_event

        self.dt_string = StringVar()

        self.clock_thread = ClockThread(self.dt_string, 1,
                                        additional_event=self.additional_event)
        self.clock_thread.start()

        statusbar = Label(master,
                          background='black',
                          fg='yellow',
                          relief='sunken', anchor='w',
                          textvariable=self.dt_string)
        statusbar.pack(anchor='s', side='bottom', fill='x')


class ClockThread(Thread):
    """
    Time update thread.
    """

    def __init__(
            self,
            time_var: StringVar,
            interval: int | float = 1,
            additional_event: StringVar = None
            ) -> None:
        Thread.__init__(self)
        self.daemon = True
        self.interval = interval
        self.time_var = time_var
        self.additional_event = additional_event

    def run(self):
        while True:
            current_time = datetime.now().strftime('%d/%b/%Y, %H:%M:%S')
            if not self.additional_event:
                self.time_var.set(current_time)
            else:
                self.time_var.set(f'{current_time}: {self.additional_event}')
            time.sleep(self.interval)
    