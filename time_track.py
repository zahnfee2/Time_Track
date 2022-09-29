import tkinter as tk
from datetime import datetime
from os.path import exists
import string

# Counter to identify start and end
counter = 0
start_time = datetime.now()

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('600x300') # change window size

# filename
filename = "working_time.csv"

time_format = '%Y/%m/%d %H:%M'

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
        header = "start;end;duration\n"
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

    else: # is not running
        # calculate the duration
        global end_time
        end_time = time_stamp

        duration = convert_to_datetime(end_time) - convert_to_datetime(start_time)

        # create line 
        str_data = str(start_time) + ";" + str(end_time) + ";" + str(duration) + '\n'

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
    print("Start_time is changend from: " + start_time_old + " to: " + start_time)
    # save_new_data_and_sort_list(datetime)



def insert_datetime(content, datetime_str):
    print(content)
    content.append(datetime_str)
    # data = sorted(content, key=lambda row: datetime.strptime(row[0], time_format))
    print("sort done")
    # return data

"""
conv_datetime = convert_to_datetime(datetime_str)
    conv_content = []

    for i in content:
        split_i = i.split(';')
        if(len(split_i) == 3):
            counter = 0
            for letter in split_i:
                if(counter == 0):
                    conv_i = convert_to_datetime(letter)
                    conv_content.append(conv_i)
                    break
"""
    

    


# save datetime in file and sort the list 
def save_new_data_and_sort_list(datetime):
    content = get_file_content(filename)
    for i in content:
        print(i)
    # sort_content = insert_datetime(content, datetime)
    # print(sort_content)
    # save_in_file(sort_content, filename, 'w')



######## Start / End Button ########
# show label while the time is recording
lab = tk.Label(frame, text="time is running ...")

# Start/End Button
btn = tk.Button(frame, text = "Start", command = track)
btn.pack()

# change the start time
change_start_time = tk.Text(frame, height=2, width=30)

# forgot label
forgot_lbl = tk.Label(frame, text="Did you forget to press start?\n  Here you have the possibility to correct the start time.")

# save button
save_button = tk.Button(frame, text="Save", command=save_correct_start)

# quit button 
quit = tk.Button(frame, text="Quit", command=frame.destroy)
quit.pack()

# main loop
frame.mainloop()
