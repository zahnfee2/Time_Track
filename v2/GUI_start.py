import tkinter
from Time_track import *
from datetime import datetime
from Handle_files import *
from include import *
from Function import *


class UI_Start():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Time Track")
        self.root.geometry('300x600')

        tkinter.Label(self.root, text="Welcome to daily.").pack(pady=15)
        tkinter.Button(self.root, text="Track Time", height=1, width=30, command=UI_Track_Time ).pack(pady=4)
        tkinter.Button(self.root, text="Show recordet time", height=1, width=30, command=UI_Show_Rec_Time ).pack(pady=4)

        tkinter.Label(self.root, text="Add Time").pack(pady=30)

        # add start time
        tkinter.Label(self.root, text="Add Start Time").pack(pady=5)
        self.add_start_time = tkinter.Text(self.root, height=1, width=17)
        self.add_start_time.insert('1.0', datetime.now().strftime(time_format))
        self.add_start_time.pack(pady=5)
    
        # add end time 
        tkinter.Label(self.root, text="Add End Time").pack(pady=5)
        self.add_end_time = tkinter.Text(self.root, height=1, width=17)
        self.add_end_time.insert('1.0', datetime.now().strftime(time_format))
        self.add_end_time.pack(pady=5)

        # add topic
        tkinter.Label(self.root, text="Add Topic").pack(pady=5)
        self.add_topic = tkinter.Text(self.root, height=3, width=33)
        self.add_topic.pack(pady=5)

        self.save_button_add_time = tkinter.Button(self.root, text="Add New Time", height=1, width=30, command=self.add_new_time ).pack(pady=5)

        # Quit Button
        tkinter.Button(self.root, text="Quit", height=1, width=30, command=quit ).pack(pady=4)

        self.root.mainloop()


    def convert_to_datetime(self, str_datetime):
        return datetime.strptime(str_datetime, time_format)


    def add_new_time(self):
        start_time_str = self.add_start_time.get(1.0, 'end-1c')
        end_time_str = self.add_end_time.get(1.0, 'end-1c')
        topic_str = self.add_topic.get(1.0, 'end-1c')

        if check_datetime_format(start_time_str) and check_datetime_format(end_time_str):
            duration = self.convert_to_datetime(end_time_str) - self.convert_to_datetime(start_time_str)
            row = [start_time_str, end_time_str, str(duration), topic_str]
            write_in_csv_file(row)
            content = get_content_csv_file(csv_path)
            content = sort_Content(content)
            write_List_in_csv(csv_path, content)
            #write_in_file(csv_path, content.dtypes, 'w')
            print("Time was added and the List is sorted")

    def quit(self):
        self.root.destroy()



class UI_Track_Time():
    def __init__(ui_track):

        # Main Window
        ui_track.win_track = tkinter.Tk()
        ui_track.win_track.title("Time Track")
        ui_track.win_track.geometry('300x350')

        ui_track.time_is_running_label = tkinter.Label(ui_track.win_track, text="Time is running!", bg="aquamarine")

        # End Button
        ui_track.end_button = tkinter.Button(ui_track.win_track, text="End Tracking", height=1, width=30, command=ui_track.end_tracking )

        # Topic Text
        ui_track.topic_label = tkinter.Label(ui_track.win_track, text="Topic:")
        ui_track.topic_Text = tkinter.Text(ui_track.win_track, height=3, width=33)

        # Start Button
        ui_track.start_button = tkinter.Button(ui_track.win_track, text="Start Tracking", height=1, width=30, command=ui_track.start_tracking )
        ui_track.start_button.pack(pady=10)

        # Change Start Time
        ui_track.change_start_time_label = tkinter.Label(ui_track.win_track, text="Change Start Time")
        ui_track.change_start_time_Text = tkinter.Text(ui_track.win_track, height=1, width=17)
        ui_track.change_start_time_Text.insert('1.0', datetime.now().strftime(time_format))
        ui_track.save_button_change_start_time = tkinter.Button(ui_track.win_track, text="Save New Start Time", height=1, width=30, command=ui_track.changeStartTime )

        # Saved Label 
        ui_track.saved_label = tkinter.Label(ui_track.win_track, bg="green", height=1, width=15, text="Saved")

        # Quit Button
        ui_track.quit_button = tkinter.Button(ui_track.win_track, text="Quit", height=1, width=30, command=quit )
        ui_track.quit_button.pack(pady=2)

        # Main Loop
        ui_track.win_track.mainloop()
    
    def changeStartTime(ui_track):
        ui_track.start_time = datetime.now()
        ui_track.saved_label.pack(pady=15)


    def compute_duration(ui_track):
        ui_track.duration = ui_track.end_time - ui_track.start_time


    def start_tracking(ui_track):
        ui_track.start_time = datetime.now()

        # convert time in a good format to save the data
        # ui_track.start_time = start_time.strftime(time_format)

        # hide start button
        ui_track.start_button.pack_forget()

        # hide quit button
        ui_track.quit_button.pack_forget()

        # show time is running label
        ui_track.time_is_running_label.pack(pady=20)

        # show end button
        ui_track.end_button.pack(pady=10)

        # show topic Textfild
        ui_track.topic_label.pack()
        ui_track.topic_Text.pack(pady=2)

        # show area save new start time
        ui_track.change_start_time_label.pack(pady=3)
        ui_track.change_start_time_Text.pack(pady=3)
        ui_track.save_button_change_start_time.pack(pady=3)


    def end_tracking(self):
        self.end_time = datetime.now()
        self.topic = self.topic_Text.get(1.0, 'end-1c')

        # show start button
        self.start_button.pack(pady=2)

        # show quit button
        self.quit_button.pack(pady=2)

        # hide time is running label
        self.time_is_running_label.pack_forget()

        # hide end button
        self.end_button.pack_forget()

        # hide topic Textfile
        self.topic_label.pack_forget()
        self.topic_Text.delete("1.0", "end")
        self.topic_Text.pack_forget()

        # hide area save new start time
        self.change_start_time_label.pack_forget()
        self.change_start_time_Text.pack_forget()
        self.save_button_change_start_time.pack_forget()

        # hide saved label (green)
        self.saved_label.pack_forget()
        
        # compute duration and save the data
        self.compute_duration()
        self.save_time()


    def save_time(self):
        start_time_str = self.start_time.strftime(time_format)
        end_tim_str = self.end_time.strftime(time_format)
        duration_str = str(self.duration)
        row = [start_time_str, end_tim_str, duration_str, self.topic]
        write_in_csv_file(row)
        

    def quit(ui_track):
        ui_track.win_track.destroy()


class UI_Show_Rec_Time():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Time Track")
        self.root.geometry('300x400')

        tkinter.Label(self.root, text="This is your recordet Time").pack(pady=10)

        self.root.mainloop()

    def quit(self):
        self.root.destroy()
