import tkinter
import tkinter.font as font
from tkinter import Canvas
from Time_track import *
from datetime import datetime, date
from Handle_files import *
import re
import include as inc
from Function import *
from tkcalendar import Calendar, DateEntry
from tktimepicker import SpinTimePickerModern
from tktimepicker import constants
from GUI.Edit_Entry import Edit_Entry


class UI_Show_Rec_Time():

    def __init__(self):
        self.root = tkinter.Tk()
        self.frame = None
        self.root.title("Time Track")
        self.root.geometry('1300x780')

        rec_font = font.Font(family='Hevetica', size=20, weight='bold')

        self.start_lb = tkinter.Label(self.root, text="This is your recordet Time", font=rec_font)
        self.start_lb.pack()
        content = get_content_csv_file(csv_path)


        date_list = content.date.tolist()
        start_list = content.start.tolist()
        end_list = content.end.tolist()
        duration_list= content.duration.tolist()
        topic_list = content.topic.tolist()

        self.text_fild = tkinter.Text(self.root, width = 150, height=30, wrap=tkinter.NONE)

        # counter
        self.counter = 1

        # add content to columns
        for i in range(0, len(start_list)):

            if duration_list[i] == '0': 
                duration_list[i] = '0:00:00'

            text_button = '\t' + str(self.counter) + '\t' + str(date_list[i]) + '\t' + str(start_list[i]) + '\t'  + str(end_list[i]) + '\t' + str(duration_list[i]) + '\t' + str(topic_list[i]) 
            tkinter.Button(self.root, text=text_button, height=1, width=100, anchor="w", command=lambda i=i:self.edit_entry(i)).pack()
            self.text_fild.insert(tkinter.END, text_button + '\n')
            self.counter = self.counter + 1

        # quit Button
        self.quit_button = tkinter.Button(self.root, text="Quit", height=1, width=30 ,command=self.quit)
        self.quit_button.pack(pady=20)
        self.root.mainloop()
    
    def edit_entry(self, counter):
        self.quit()
        Edit_Entry(counter)

    def quit(self):
        self.root.destroy()
