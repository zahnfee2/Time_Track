import tkinter
import tkinter.font as font
from tkinter import ttk
from tkinter import Canvas
from Handle_files import *
from include import *
from Function import *
import re
import GUI.Show_Rec
from tkcalendar import Calendar, DateEntry
from tktimepicker import AnalogPicker, constants
from datetime import datetime, date


class Edit_Entry():

    def __init__(self, i):
        self.counter = i
        self.root = tkinter.Tk()
        self.root.title("Counter: " + str(i))
        self.root.geometry('380x980')

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

        self.content = get_content_csv_file(csv_path)
        self.chosen_row = self.content.iloc[i]


        # Start Time 
        tkinter.Label(self.second_frame, text="Start Time: ").pack(pady=15)
        self.picker_start = AnalogPicker(self.second_frame, type=constants.HOURS24) #take out 'period=constants.PM' to change to AM
        start_time_hour = datetime.strptime(self.chosen_row['start'], time_format).hour
        start_time_min = datetime.strptime(self.chosen_row['start'], time_format).minute
        self.picker_start.setHours(start_time_hour) 
        self.picker_start.setMinutes(start_time_min) 
        self.picker_start.pack(fill="both")

        # End Time 
        tkinter.Label(self.second_frame, text="End Time: ").pack(pady=15)
        self.picker_end = AnalogPicker(self.second_frame, type=constants.HOURS24) #take out 'period=constants.PM' to change to AM
        end_time_hour = datetime.strptime(self.chosen_row['end'], time_format).hour
        end_time_min = datetime.strptime(self.chosen_row['end'], time_format).minute
        self.picker_end.setHours(end_time_hour)
        self.picker_end.setMinutes(end_time_min) 
        self.picker_end.pack(fill="both")

        # date picker
        tkinter.Label(self.second_frame, text="Duration: ").pack(pady=15)
        tkinter.Label(self.second_frame, text='Choose date').pack(padx=10, pady=5)
        self.start_cal = DateEntry(self.second_frame
                                   , width=12
                                   , background='darkblue'
                                   ,foreground='white'
                                   , borderwidth=2
                                   , year=datetime.strptime(self.chosen_row['date'], date_format).year
                                   , month=datetime.strptime(self.chosen_row['date'], date_format).month
                                   , day=datetime.strptime(self.chosen_row['date'], date_format).day
                                   )
        self.start_cal.pack(padx=10, pady=5)

        # add topic
        tkinter.Label(self.second_frame, text="Topic").pack(pady=5)
        self.add_topic = tkinter.Text(self.second_frame, height=4, width=50)
        self.add_topic.insert(tkinter.INSERT, str(self.chosen_row['topic']))
        self.add_topic.pack(pady=5)

        # add save buton 
        tkinter.Button(self.second_frame, text="Save", height=2, width=30, fg='green', command=self.save_entry ).pack(pady=5)


        # Error Label 
        self.start_bigger_end = tkinter.Label(self.second_frame, text="Start muss kleiner sein als Ende.", bg='red')

        # quit Button
        self.quit_button = tkinter.Button(self.second_frame, text="Quit", height=1, width=30 ,command=self.quit)
        self.quit_button.pack(pady=3)

        # Delete Button 
        tkinter.Button(self.second_frame, text="Delete Entry", height=1, width=10 ,fg='red', command=self.delete_entry).pack(pady=15)

        self.root.mainloop()

    def delete_entry(self):
        self.delet_root = tkinter.Tk()
        self.delet_root.geometry("100x100")
        tkinter.Label(self.delet_root, text="Are you sure?").pack()
        tkinter.Button(self.delet_root, text="DELETE", command=self.delete, fg='red').pack()
        tkinter.Button(self.delet_root, text="Cancel", command=self.quit_delete_window).pack()
    
    def quit_delete_window(self):
        self.delet_root.destroy()

    def delete(self):
        self.content = self.content.drop(self.counter)
        self.content = sort_Content(self.content)
        write_List_in_csv(csv_path, self.content)
        self.quit_delete_window()
        self.quit()
        GUI.Show_Rec.UI_Show_Rec_Time()



    def convert_time(self, time):
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
            self.content.iloc[self.counter]['date'] = date
            self.content.iloc[self.counter]['start'] = start_time
            self.content.iloc[self.counter]['end'] = end_time
            self.content.iloc[self.counter]['duration'] = duration
            self.content.iloc[self.counter]['topic'] = topic

            self.content = sort_Content(self.content)
            write_List_in_csv(csv_path, self.content)
            self.quit()
            GUI.Show_Rec.UI_Show_Rec_Time()


    def quit(self):
        self.root.destroy()
        GUI.Show_Rec.UI_Show_Rec_Time()
