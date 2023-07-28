import tkinter
import tkinter.font as font
from tkinter import Canvas
from turtle import width
from Time_track import *
from datetime import datetime, date
from Handle_files import *
import include as inc
from Function import *
from tkcalendar import Calendar, DateEntry
from tktimepicker import SpinTimePickerModern
from tktimepicker import constants
from GUI.Edit_Entry import Edit_Entry
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "green"
)  # Themes: blue (default), dark-blue, green


class UI_Show_Rec_Time:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title("Time Track")
        self.root.geometry("1300x600")

        # Button Frame
        self.button_frame = customtkinter.CTkScrollableFrame(
            self.root, width=200, height=200
        )
        self.button_frame.pack(pady=3, padx=0, fill="both", expand=True)

        # Create A Main Frame
        self.main_frame = customtkinter.CTkFrame(self.root, width=10, height=10)
        self.main_frame.pack(pady=0, padx=0, fill=None, expand=False)

        rec_font = font.Font(family="Hevetica", size=20, weight="bold")

        content = get_content_csv_file(csv_path)

        date_list = content.date.tolist()
        start_list = content.start.tolist()
        end_list = content.end.tolist()
        duration_list = content.duration.tolist()
        topic_list = content.topic.tolist()

        self.text_fild = customtkinter.CTkTextbox(self.button_frame)

        # counter
        self.counter = 1

        # add content to columns
        for i in range(0, len(start_list)):
            if duration_list[i] == "0":
                duration_list[i] = "0:00:00"

            text_button = (
                "\t"
                + str(self.counter)
                + "\t"
                + str(date_list[i])
                + "\t"
                + str(start_list[i])
                + "\t"
                + str(end_list[i])
                + "\t"
                + str(duration_list[i])
                + "\t"
                + str(topic_list[i])
            )
            customtkinter.CTkButton(
                self.button_frame,
                text=text_button,
                width=2000,
                anchor="w",
                command=lambda i=i: self.edit_entry(i),
            ).pack(pady=3, padx=1)
            self.text_fild.insert("0.0", text_button + "\n")
            self.counter = self.counter + 1

        # quit Button
        self.quit_button = customtkinter.CTkButton(
            self.main_frame, text="Quit", command=self.quit
        )
        self.quit_button.pack(pady=20)
        self.root.mainloop()

    def edit_entry(self, counter):
        self.quit()
        Edit_Entry(counter)

    def quit(self):
        self.root.destroy()
