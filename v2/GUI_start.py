import tkinter
from Time_track import *
from datetime import datetime
from Handle_files import *
from include import *


class UI_Start():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Time Track")
        self.root.geometry('300x200')

        tkinter.Label(self.root, text="Welcome to daily.").pack(pady=20)
        tkinter.Button(self.root, text="Track Time", height=1, width=15, command=UI_Track_Time ).pack(pady=4)
        tkinter.Button(self.root, text="Show recordet time", height=1, width=15, command=UI_Show_Rec_Time ).pack(pady=4)

        self.root.mainloop()

    def quit(self):
        self.root.destroy()



class UI_Track_Time():
    def __init__(ui_track):

        # Main Window
        ui_track.win_track = tkinter.Tk()
        ui_track.win_track.title("Time Track")
        ui_track.win_track.geometry('300x200')

        # End Button
        ui_track.end_button = tkinter.Button(ui_track.win_track, text="End Tracking", height=1, width=15, command=ui_track.end_tracking )

        # Topic Text
        ui_track.topic_label = tkinter.Label(ui_track.win_track, text="Topic:")
        ui_track.topic_Text = tkinter.Text(ui_track.win_track, height=2, width=30)

        # Start Button
        ui_track.start_button = tkinter.Button(ui_track.win_track, text="Start Tracking", height=1, width=15, command=ui_track.start_tracking )
        ui_track.start_button.pack(pady=2)

        # Quit Button
        ui_track.quit_button = tkinter.Button(ui_track.win_track, text="Quit", height=1, width=15, command=quit )
        ui_track.quit_button.pack(pady=2)

        # Main Loop
        ui_track.win_track.mainloop()
    

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

        # show end button
        ui_track.end_button.pack(pady=2)

        # show topic Textfild
        ui_track.topic_label.pack()
        ui_track.topic_Text.pack(pady=2)


    def end_tracking(self):
        self.end_time = datetime.now()
        self.topic = self.topic_Text.get(1.0, 'end-1c')

        # show start button
        self.start_button.pack(pady=2)

        # show quit button
        self.quit_button.pack(pady=2)

        # hide end button
        self.end_button.pack_forget()

        # hide topic Textfile
        self.topic_label.pack_forget()
        self.topic_Text.delete("1.0", "end")
        self.topic_Text.pack_forget()
        
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

