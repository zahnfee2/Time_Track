import customtkinter
import tkinter
import tkinter.font as font
from tkinter import Canvas
from Handle_files import *
from include import *
from Function import *
import re
from tkcalendar import Calendar, DateEntry
from tktimepicker import AnalogPicker, constants
from datetime import datetime, date


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

class Add_Entry():

    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title("Add time")
        self.root.geometry('450x900')

        # Create A Main Frame
        self.main_frame = customtkinter.CTkScrollableFrame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Abort Frame
        self.abort_frame = customtkinter.CTkFrame(self.root)
        self.abort_frame.pack(fill=None, expand=False)

        # Start Time 
        customtkinter.CTkLabel(self.main_frame, text="Start Time: ").pack(pady=15)
        self.picker_start = AnalogPicker(self.main_frame, type=constants.HOURS24) #take out 'period=constants.PM' to change to AM
        self.picker_start.setHours(datetime.now().hour)
        self.picker_start.setMinutes(datetime.now().minute) 
        self.picker_start.pack(fill="both")

        # End Time 
        customtkinter.CTkLabel(self.main_frame, text="End Time: ").pack(pady=15)
        self.picker_end = AnalogPicker(self.main_frame, type=constants.HOURS24) #take out 'period=constants.PM' to change to AM
        self.picker_end.setHours(datetime.now().hour)
        self.picker_end.setMinutes(datetime.now().minute) 
        self.picker_end.pack(fill="both")

        # Date picker
        customtkinter.CTkLabel(self.main_frame, text='Choose date').pack(padx=10, pady=5)
        self.start_cal = DateEntry(self.main_frame
                                   , width=12
                                   , background='darkblue'
                                   ,foreground='white'
                                   , borderwidth=2
                                   , year=datetime.now().year
                                   , month=datetime.now().month
                                   , day=datetime.now().day
                                   )
        self.start_cal.pack(padx=10, pady=5)

        # Add topic
        customtkinter.CTkLabel(self.main_frame, text="Topic").pack(pady=5)
        self.add_topic = customtkinter.CTkTextbox(self.main_frame)
        self.add_topic.pack(fill="x", expand=True, pady=5, padx=5)

        # Add save buton 
        customtkinter.CTkButton(self.main_frame, text="Save", command=self.save_entry ).pack(pady=5)

        # Error Label 
        self.start_bigger_end = customtkinter.CTkLabel(self.main_frame, text="Start muss kleiner sein als Ende.")

        # quit Button
        self.quit_button = customtkinter.CTkButton(self.abort_frame, text="Quit", command=self.quit)
        self.quit_button.pack(pady=3)
        self.root.mainloop()

    def convert_time(self, time):
        # get the numbers from the ugly time 
        numbers = re.findall(r'\b\d+\b', time)
        new_time = numbers[0] + ':' + numbers[1]
        return new_time
    
    def save_entry(self): 
        date = self.start_cal.get_date()
        start_time = self.convert_time(str(self.picker_start.time()))
        start_time = datetime.strptime(start_time , time_format)
        end_time = self.convert_time(str(self.picker_end.time()))
        end_time = datetime.strptime(end_time, time_format)
        if(start_time > end_time):
            self.start_bigger_end.pack()
        else: 
            self.start_bigger_end.forget()
            duration = end_time - start_time
            topic = self.add_topic.get("0.0", "end")
            row = [date,start_time.strftime(time_format), end_time.strftime(time_format), duration, topic]
            write_in_csv_file(row)
            content = get_content_csv_file(csv_path)
            content = sort_Content(content)
            write_List_in_csv(csv_path, content)
            push_tracked_time()
            self.quit()

    def quit(self):
        self.root.destroy()
