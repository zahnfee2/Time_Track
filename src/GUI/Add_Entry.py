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


class Add_Entry():

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Add time")
        self.root.geometry('450x900')

        # Create A Main Frame
        main_frame = tkinter.Frame(self.root)
        main_frame.pack(fill=tkinter.BOTH, expand=1)

        # Create A Canvas 
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

        # Add A Scrollbar To The Canvas 
        my_scrollbar = tkinter.Scrollbar(main_frame, orient=tkinter.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Configure The Canvas 
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE The Canvas 
        self.second_frame = tkinter.Frame(my_canvas)

        # Add That New Frame To A Window In the Canvas
        my_canvas.create_window((0,0), window=self.second_frame, anchor="nw")


        headers = font.Font(family='Hevetica', size=30, weight='bold')

        # Start Time 
        tkinter.Label(self.second_frame, text="Start Time: ", font=headers).pack(pady=15)
        self.picker_start = AnalogPicker(self.second_frame, type=constants.HOURS24) #take out 'period=constants.PM' to change to AM
        self.picker_start.setHours(datetime.now().hour)
        self.picker_start.setMinutes(datetime.now().minute) 
        self.picker_start.pack(fill="both")

        # End Time 
        tkinter.Label(self.second_frame, text="End Time: ", font=headers).pack(pady=15)
        self.picker_end = AnalogPicker(self.second_frame, type=constants.HOURS24) #take out 'period=constants.PM' to change to AM
        self.picker_end.setHours(datetime.now().hour)
        self.picker_end.setMinutes(datetime.now().minute) 
        self.picker_end.pack(fill="both")

        # Date picker
        tkinter.Label(self.second_frame, text='Choose date').pack(padx=10, pady=5)
        self.start_cal = DateEntry(self.second_frame
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
        tkinter.Label(self.second_frame, text="Topic").pack(pady=5)
        self.add_topic = tkinter.Text(self.second_frame, height=4, width=50)
        self.add_topic.pack(pady=5)

        # Add save buton 
        tkinter.Button(self.second_frame, text="Save", height=1, width=30, command=self.save_entry ).pack(pady=5)

        # Error Label 
        self.start_bigger_end = tkinter.Label(self.second_frame, text="Start muss kleiner sein als Ende.", bg='red')

        # quit Button
        self.quit_button = tkinter.Button(self.second_frame, text="Quit", height=1, width=30 ,command=self.quit)
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
            topic = self.add_topic.get(1.0, 'end-1c')
            row = [date,start_time.strftime(time_format), end_time.strftime(time_format), duration, topic]
            write_in_csv_file(row)
            content = get_content_csv_file(csv_path)
            content = sort_Content(content)
            write_List_in_csv(csv_path, content)
            self.quit()

    def quit(self):
        self.root.destroy()
