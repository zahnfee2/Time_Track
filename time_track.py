import tkinter as tk
from datetime import datetime
from os.path import exists
from turtle import st
import pandas as pd

# Counter to identify start and end
counter = 0

# time format 
time_format = '%Y/%m/%d %H:%M'

# chreate start time 
start_time = datetime.now()
start_time = start_time.strftime(time_format)

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('600x300') # change window size

# filename
filename = "working_time.csv"


# save string in file
def save_in_file(content, filename, operation):
    # open file
    f = open(filename, operation)

    # write content in fiel
    f.write(str(content))
    
    # close file
    f.close()


# write the timestamp in a file
def track():

    # create timestamp
    time_stamp = datetime.now()
    time_stamp = time_stamp.strftime(time_format)


    # check if file exists 
    if not exists(filename):
        header = "start,end,duration\n"
        save_in_file(header, filename, 'a')

    # check if start or end
    global counter 
    counter = counter + 1
    if counter % 2 == 1: # is running

        # compute working time
        global start_time 
        start_time = time_stamp

        # change button text
        btn['text'] = 'End'

        # unhide label
        lab.pack()

        # hide quit button
        quit.pack_forget()

        # show correct text fild
        forgot_lbl.pack()
        change_start_time.pack()
        change_start_time.insert('1.0', str(start_time))

        # show save button
        save_button.pack()

        # hide add time
        add_start_time_lbl.pack_forget()
        add_end_time_lbl.pack_forget()
        add_start_time.pack_forget()
        add_end_time.pack_forget()
        add_time_save.pack_forget()

    else: # is not running
        # calculate the duration
        global end_time
        end_time = time_stamp

        duration = convert_to_datetime(end_time) - convert_to_datetime(start_time)

        # create line 
        str_data = str(start_time) + "," + str(end_time) + "," + str(duration) + '\n'

        # insert a new line in the file
        save_in_file(str_data, filename, 'a')

        # change button text
        btn['text'] = 'Start'

        # hide label
        lab.pack_forget()

        # unhide quit button
        quit.pack()

        # hide correct button 
        forgot_lbl.pack_forget()
        change_start_time.pack_forget()

        # hide save button
        save_button.pack_forget()

        # show add time 
        add_start_time_lbl.pack()
        add_end_time_lbl.pack()
        add_start_time.pack()
        #add_start_time.insert('1.0', str(start_time))
        add_end_time.pack()
        #add_end_time.insert('1.0', str(start_time))
        add_time_save.pack()

        # hide saved label
        saved_lbl.pack_forget()

def convert_to_datetime(str_datetime):
    return datetime.strptime(str_datetime, time_format)

# get file content
def get_file_content(filename):
    content = []
    with open(filename, 'r') as f:
        f.readline()
        for line in f: 
            content.append(str(line))

    return content


# save date time in file 
def save_correct_start():
    global start_time
    start_time_old = start_time
    start_time = str(change_start_time.get(1.0, 'end-1c'))
    saved_lbl.pack()




def sort_list_by_datetime(content):#
    data = sorted(content, key=lambda row: datetime.strptime(row[0], time_format))
    print("sort done")
    return data

    
def save_time():
    new_start_time = add_start_time.get(1.0, 'end-1c')
    new_end_time = add_end_time.get(1.0, 'end-1c')
    new_duration = convert_to_datetime(new_end_time) - convert_to_datetime(new_start_time)

    line = {'start': str(new_start_time) 
    , 'end': str(new_end_time) 
    , 'duration': str(new_duration)}
    


    content = pd.read_csv(filename)
    content = pd.DataFrame(content)
    content = content.append(line, ignore_index=True)
    print(content.head())
    content['start'] = pd.to_datetime(content.start, infer_datetime_format = True)
    content.sort_values(by='start', ascending=True, inplace=True)

    content.to_csv(filename, index=False)
    print(content.head())

    print("List was sorted!")


# print a list on the consol 
def print_list(list):
    for i in list:
        print(i)



######## Start / End Button ########
# show label while the time is recording
lab = tk.Label(frame, text="time is running ...")

# Start/End Button
btn = tk.Button(frame, text = "Start", command = track)
btn.pack()

# forgot label
forgot_lbl = tk.Label(frame,text="Did you forget to press start?\n  Here you have the possibility to correct the start time.")

saved_lbl = tk.Label(frame,text="Saved!")

# change the start time
change_start_time = tk.Text(frame, height=2, width=30)

# save button
save_button = tk.Button(frame, text="Save", command=save_correct_start)

# add start time
add_start_time_lbl = tk.Label(frame, text="Start Time:")
add_start_time_lbl.pack()
add_start_time = tk.Text(frame, height=2, width=30)
add_start_time.insert('1.0', str(start_time))
add_start_time.pack()

# add end time
add_end_time_lbl = tk.Label(frame, text="End Time:")
add_end_time_lbl.pack()
add_end_time = tk.Text(frame, height=2, width=30)
add_end_time.insert('1.0', str(start_time))
add_end_time.pack()

# save button to add new time 
add_time_save = tk.Button(frame, text="Save", command=save_time)
add_time_save.pack()

# quit button 
quit = tk.Button(frame, text="Quit", command=frame.destroy)
quit.pack()

# main loop
frame.mainloop()
