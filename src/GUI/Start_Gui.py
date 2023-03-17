import tkinter
import tkinter.font as font
from tkinter import Canvas
from Time_track import *
from datetime import datetime, date
from Handle_files import *
import re
import include as inc
from GUI.Show_Rec import UI_Show_Rec_Time
from GUI.Start_Rec import UI_Track_Time
from GUI.Add_Entry import Add_Entry
from Function import *

class UI_Start():
    def __init__(self):

        create_file_if_not_exists()

        if check_If_gitrepo_exists():
            if inc.connect_csv_with_git:
                pull_tracked_time()

        self.root = tkinter.Tk()
        self.root.title("Time Track")
        self.root.geometry('370x820')

        # Front for heading
        header = font.Font(family='Hevetica', size=30, weight='bold')

        # header
        tkinter.Label(self.root, text="Welcome to daily.", font=header).pack(pady=15)

        # show the entire duration
        tkinter.Label(self.root, text="Duration: " + str(get_entire_duration())).pack(pady=15)

        # Start tracking time
        tkinter.Button(self.root, text="Track Time",height=1, width=30, command=self.start_tracking_time).pack(pady=4)

        # Show the entrys 
        tkinter.Button(self.root, text="Show recordet time", height=1, width=30, command=self.show_rec_time ).pack(pady=4)

        # Add git switch to sync the csv file with a git repro
        tkinter.Label(self.root, text='Synchronize data with git:').pack(pady=4)
        self.sync_with_git_button = tkinter.Button(self.root, text=self.getSwitchValue(), height=1, width=5, command=self.change_git_sync)
        self.sync_with_git_button.pack(pady=4)

        # Add Label if git repo does not exists 
        self.noGitReproLabel = tkinter.Label(self.root, bg="red", text="Git Repo does not exists!")

        # Line 
        canvas = Canvas(self.root, width=350, height=30)
        canvas.create_line(0, 15, 350, 15)
        canvas.pack()

        # Add new Time 
        self.button = tkinter.Button(self.root, text="Add Time", height=1, width=30, command=self.add_time).pack()

        # Add line 
        canvas = Canvas(self.root, width=350, height=30)
        canvas.create_line(0, 15, 350, 15)
        canvas.pack()

        # Quit Button
        tkinter.Button(self.root, text="Quit", height=1, width=30, command=self.quit ).pack(pady=2)

        self.root.mainloop()
    
    def add_time(self):
        Add_Entry()

    def getSwitchValue(self):
        if inc.connect_csv_with_git:
            return "ON"
        return "OFF"

    def change_git_sync(self):
        if check_If_gitrepo_exists():
            if inc.connect_csv_with_git:
                inc.connect_csv_with_git = False
                self.sync_with_git_button['text'] = "OFF"
            else:
                inc.connect_csv_with_git = True
                self.sync_with_git_button['text'] = "ON"
                pull_tracked_time()
        else: 
            self.noGitReproLabel.pack(pady=4)
            
    def show_rec_time(self):
        UI_Show_Rec_Time()

    def start_tracking_time(self):
        UI_Track_Time()
    
    def convert_to_datetime(self, str_datetime):
        return datetime.strptime(str_datetime, time_format)

    # Example of time 2023-03-17(23, 59, 'AM')
    def convert_time(self, time):
        # get the numbers from the ugly time 
        numbers = re.findall(r'\b\d+\b', time)
        new_time = numbers[0] + ':' + numbers[1]
        return new_time

    def quit(self):
        self.root.destroy()
