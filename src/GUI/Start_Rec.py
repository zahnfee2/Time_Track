from turtle import width
from Time_track import *
from datetime import datetime, date
from Handle_files import *
import re
import include as inc
from Function import *
from tkcalendar import Calendar, DateEntry
from tktimepicker import SpinTimePickerModern, AnalogPicker
from tktimepicker import constants
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
class UI_Track_Time():
    def __init__(self):
        self.date = date.today()

        self.start_time = datetime.now().strftime(time_format)

        self.root = customtkinter.CTk()
        self.root.title("Record Time")
        self.root.geometry('300x800')

        # Main Window
        self.win_track = customtkinter.CTkFrame(master=self.root)
        self.win_track.pack(pady=0, padx=0, fill="both", expand=True)

        self.time_is_running_label = customtkinter.CTkLabel(self.win_track, text="Time is running!")

        # End Button
        self.end_button = customtkinter.CTkButton(self.win_track, text="End Tracking", command=self.end_tracking )

        # Topic Text
        self.topic_label = customtkinter.CTkLabel(self.win_track, text="Topic:")
        self.topic_Text = customtkinter.CTkTextbox(self.win_track)

        # Change Start Time
        self.change_start_time_label = customtkinter.CTkLabel(self.win_track, text="Change Start Time")
        self.save_button_change_start_time = customtkinter.CTkButton(self.win_track, text="Save New Start Time", command=self.changeStartTime )

        # start time picker
        self.time_picker_start = AnalogPicker(self.win_track, type=constants.HOURS24)
        self.time_picker_start.setHours(datetime.now().hour) 
        self.time_picker_start.setMinutes(datetime.now().minute) 

        # Saved Label 
        self.saved_label = customtkinter.CTkLabel(self.win_track, text="Saved")

        # Quit Button
        self.quit_button = customtkinter.CTkButton(self.win_track, text="Cancel", command=self.quit )

        # overlap 
        self.overlap = customtkinter.CTkLabel(self.win_track, text="Time overlaps with on other")
        self.start_time = datetime.now().strftime(time_format)

        # show time is running label
        self.time_is_running_label.pack(pady=20)

        # show end button
        self.end_button.pack(pady=10)

        # show topic Textfild
        self.topic_label.pack()
        self.topic_Text.pack(pady=2, padx=2, fill="x", expand=False)

        # show area save new start time
        self.change_start_time_label.pack(pady=3)
        self.time_picker_start.pack( fill="both")
        self.save_button_change_start_time.pack(pady=3)

        # Cancel Button
        self.quit_button.pack(pady=2)

        # Main Loop
        self.win_track.mainloop()

    def convert_time(self, time):
        # get the numbers from the ugly time 
        numbers = re.findall(r'\b\d+\b', time)
        new_time = numbers[0] + ':' + numbers[1]
        return new_time
        
    def convert_to_datetime(self, str_datetime):
        return datetime.strptime(str_datetime, time_format)
    
    def changeStartTime(self):
        enter = str(self.time_picker_start.time())
        enter = self.convert_time(enter)

        self.start_time = datetime.strptime(enter, time_format)
        self.saved_label.pack(pady=10)

    def compute_duration(self):
        if isinstance(self.end_time, str): 
            self.end_time = datetime.strptime(self.end_time, time_format)
        if isinstance(self.start_time, str):
            self.start_time = datetime.strptime(self.start_time, time_format)
        result = self.end_time - self.start_time
        if not result:
            return 0 
        else: 
            return result 

    def disable_event(self):
        pass

    def end_tracking(self):
        self.end_time = datetime.now().strftime(time_format)
        self.topic = self.topic_Text.get("0.0", "end")
        self.topic = delete_new_Line(self.topic)
        self.duration = self.compute_duration()
        if self.save_time():
            self.quit()
        

    def save_time(self):
        date_str = self.date
        duration_str = str(self.duration)
        row = [date_str, self.start_time.strftime(time_format), self.end_time.strftime(time_format), duration_str, self.topic]
        # if check_overlap(row): 
        self.overlap.pack(pady=5)
        #     return False
        # else: 
        write_in_csv_file(row)
        # sort content of file
        content = get_content_csv_file(csv_path)
        content = sort_Content(content)
        write_List_in_csv(csv_path, content)
        push_tracked_time()
        self.overlap.pack_forget()
        return True


    def quit(self):
        self.root.destroy()
