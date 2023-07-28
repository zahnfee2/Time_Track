from tkinter import Canvas, Frame

import customtkinter

from Time_track import *
from datetime import datetime, date
from Handle_files import *
import re
import include as inc
from GUI.Show_Rec import UI_Show_Rec_Time
from GUI.Start_Rec import UI_Track_Time
from GUI.Add_Entry import Add_Entry
from Function import *
from PIL import Image, ImageTk


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "green"
)  # Themes: blue (default), dark-blue, green


class UI_Start:
    def __init__(self):
        create_file_if_not_exists()

        if check_If_gitrepo_exists():
            if inc.connect_csv_with_git:
                pull_tracked_time()

        self.main = customtkinter.CTk()
        self.main.title("Time Track")
        self.main.geometry("300x300")

        ico = Image.open("./src/GUI/Icon.png")
        photo = ImageTk.PhotoImage(ico)
        self.main.wm_iconphoto(False, photo)

        self.root = customtkinter.CTkFrame(master=self.main)
        self.root.pack(pady=0, padx=0, fill="both", expand=True)

        # show the entire duration
        customtkinter.CTkLabel(
            master=self.root, text="Duration: " + str(get_entire_duration())
        ).pack(pady=5, padx=5)

        # Start tracking time
        customtkinter.CTkButton(
            self.root, text="Track Time", command=self.start_tracking_time
        ).pack(pady=5, padx=5)

        # Show the entrys
        customtkinter.CTkButton(
            self.root, text="Show recordet time", command=self.show_rec_time
        ).pack(pady=5, padx=5)

        # Add git switch to sync the csv file with a git repro
        switch_var = customtkinter.StringVar(value=self.getSwitchValue())
        self.sync_with_git_switcher = customtkinter.CTkSwitch(
            master=self.root,
            text="Sync with Git",
            command=self.change_git_sync,
            variable=switch_var,
            onvalue="on",
            offvalue="off",
        ).pack(pady=5, padx=5)

        # Add Label if git repo does not exists
        self.noGitReproLabel = customtkinter.CTkLabel(
            self.root, text="Git Repo does not exists!"
        )

        # Add new Time
        self.button = customtkinter.CTkButton(
            self.root, text="Add Time", command=self.add_time
        ).pack(pady=10, padx=5)

        # Quit Button
        customtkinter.CTkButton(self.root, text="Quit", command=self.quit).pack(
            pady=10, padx=5
        )

        self.root.mainloop()

    def add_time(self):
        Add_Entry()

    def getSwitchValue(self):
        if inc.connect_csv_with_git:
            return "on"
        return "off"

    def change_git_sync(self):
        if check_If_gitrepo_exists():
            if inc.connect_csv_with_git:
                inc.connect_csv_with_git = False
                # self.sync_with_git_button['text'] = "OFF"
            else:
                inc.connect_csv_with_git = True
                # self.sync_with_git_button['text'] = "ON"
                print("On")
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
        numbers = re.findall(r"\b\d+\b", time)
        new_time = numbers[0] + ":" + numbers[1]
        return new_time

    def quit(self):
        self.main.destroy()
