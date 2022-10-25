import tkinter
from pathlib import Path
from Time_track import *
from datetime import datetime

class UI_Start():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Time Track")
        self.root.geometry('300x400')

        tkinter.Label(self.root, text="Welcome to daily.").pack()
        tkinter.Button(self.root, text="Open", height=1, width=15, command=lambda: UI_Track_Time() ).pack(pady=2)

        self.root.mainloop()

    def quit(self):
        self.root.destroy()


class UI_Track_Time():
    def __init__(ui_track):
        ui_track.win_track = tkinter.Tk()
        ui_track.win_track.title("Time Track")
        ui_track.win_track.geometry('200x200')

        tkinter.Label(ui_track.win_track, text="Welcome to daily.").pack()
        tkinter.Button(ui_track.win_track, text="See entries", height=1, width=15, command=start_tracking ).pack(pady=2)

        tkinter.Button(ui_track.win_track, text="Quit", height=1, width=15, command=quit ).pack()
        ui_track.win_track.mainloop()
    
    def quit(ui_track):
        ui_track.win_track.destroy()


def start_tracking():

    time_format = '%Y/%m/%d %H:%M'
    start_time = datetime.now()
    start_time = start_time.strftime(time_format)
    end_time = datetime.now()
    end_time = end_time.strftime(time_format)
    t = Time_track(start_time)
    print(t)

