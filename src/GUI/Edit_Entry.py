import customtkinter
from Handle_files import *
from include import *
from Function import *
import re
import GUI.Show_Rec
from tkcalendar import Calendar, DateEntry
from tktimepicker import AnalogPicker, constants
from datetime import datetime, date

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

class Edit_Entry():

    def __init__(self, i):
        self.counter = i

        self.root = customtkinter.CTk()
        self.root.title("Counter: " + str(i))
        self.root.geometry('380x880')

        self.frame = customtkinter.CTkScrollableFrame(self.root, width=200, height=200)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)

        self.abort_frame = customtkinter.CTkFrame(self.root)
        self.abort_frame.pack(pady=0, padx=0, fill=None, expand=False)

        self.content = get_content_csv_file(csv_path)
        self.chosen_row = self.content.iloc[i]

        # Start Time 
        customtkinter.CTkLabel(self.frame, text="Start Time: ").pack(pady=15)
        self.picker_start = AnalogPicker(self.frame, type=constants.HOURS24) #take out 'period=constants.PM' to change to AM
        start_time_hour = datetime.strptime(self.chosen_row['start'], time_format).hour
        start_time_min = datetime.strptime(self.chosen_row['start'], time_format).minute
        self.picker_start.setHours(start_time_hour) 
        self.picker_start.setMinutes(start_time_min) 
        self.picker_start.pack(fill="both")

        # End Time 
        customtkinter.CTkLabel(self.frame, text="End Time: ").pack(pady=15)
        self.picker_end = AnalogPicker(self.frame, type=constants.HOURS24) #take out 'period=constants.PM' to change to AM
        end_time_hour = datetime.strptime(self.chosen_row['end'], time_format).hour
        end_time_min = datetime.strptime(self.chosen_row['end'], time_format).minute
        self.picker_end.setHours(end_time_hour)
        self.picker_end.setMinutes(end_time_min) 
        self.picker_end.pack(fill="both")

        # date picker
        customtkinter.CTkLabel(self.frame, text="Duration: ").pack(pady=15)
        customtkinter.CTkLabel(self.frame, text='Choose date').pack(padx=10, pady=5)
        self.start_cal = DateEntry(self.frame
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
        customtkinter.CTkLabel(self.frame, text="Topic").pack(pady=5)
        self.add_topic = customtkinter.CTkTextbox(self.frame)
        self.add_topic.insert("0.0", str(self.chosen_row['topic']))
        self.add_topic.pack(pady=5)

        # add save buton 
        customtkinter.CTkButton(self.frame, text="Save", command=self.save_entry ).pack(pady=5)

        # Error Label 
        self.start_bigger_end = customtkinter.CTkLabel(self.frame, text="Start muss kleiner sein als Ende.")

        # quit Button
        self.quit_button = customtkinter.CTkButton(self.abort_frame, text="Quit", command=self.quit)
        self.quit_button.pack(pady=3)

        # Delete Button 
        customtkinter.CTkButton(self.frame, text="Delete Entry", command=self.delete_entry).pack(pady=15)

        self.root.mainloop()

    def delete_entry(self):
        self.delet_root = customtkinter.CTk()
        self.delet_root.geometry("100x100")
        customtkinter.CTkLabel(self.delet_root, text="Are you sure?").pack(pady=3, padx=3)
        customtkinter.CTkButton(self.delet_root, text="DELETE", command=self.delete).pack(pady=3, padx=3)
        customtkinter.CTkButton(self.delet_root, text="Cancel", command=self.quit_delete_window).pack(pady=3, padx=3)
        self.delet_root.mainloop()
    
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
            topic = self.add_topic.get("0.0", "end")
            self.content.iloc[self.counter]['date'] = date
            self.content.iloc[self.counter]['start'] = start_time
            self.content.iloc[self.counter]['end'] = end_time
            self.content.iloc[self.counter]['duration'] = duration
            self.content.iloc[self.counter]['topic'] = topic

            self.content = sort_Content(self.content)
            write_List_in_csv(csv_path, self.content)
            push_tracked_time()
            self.quit()
            GUI.Show_Rec.UI_Show_Rec_Time()


    def quit(self):
        self.root.destroy()
        GUI.Show_Rec.UI_Show_Rec_Time()
