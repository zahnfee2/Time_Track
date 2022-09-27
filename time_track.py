import tkinter as tk
from datetime import datetime
from os.path import exists
from tkcalendar import Calendar

# Counter to identify start and end
counter = 0
start_time = datetime.now()

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('600x400')

# write the timestamp in a file
def track():

    # create timestamp
    time_stamp = datetime.now()

    # filename
    filename = "working_time.csv"

    # check if file exists 
    if not exists(filename):
        # open file
        f = open(filename, "a")
        
        # write the header in the file
        f.write("start;end;duration\n")

        # close 
        f.close()

    # open file
    f = open(filename, "a")

    # create file content
    text = str(time_stamp) + ';'

    # write content in fiel
    f.write(text)

    # check if start or end
    global counter 
    counter = counter + 1
    if counter % 2 == 1:

        # compute working time
        global start_time 
        start_time = time_stamp

        # change button text
        btn['text'] = 'End'

        # unhide label
        lab.pack()

        # hide quit button
        quit.pack_forget()

    else:
        # calculate the duration
        end_time = time_stamp
        duration = end_time - start_time

        # insert a new line in the file
        f.write(str(duration) + '\n')

        # change button text
        btn['text'] = 'Start'

        # hide label
        lab.pack_forget()

        # unhide quit button
        quit.pack()

    f.close()

# gettin date from the calendar
def fetch_date():
    date.config(text = "Selected Date is: " + tkc.get_date())


# show label while the time is recording
lab = tk.Label(frame, text="time is running ...")

# Start/End Button
btn = tk.Button(frame, text = "Start", command = track)
btn.pack()


# Calendar picker
tkc = Calendar(frame,selectmode = "day",year=2022,month=10,date=1)
tkc.pack()
but = tk.Button(frame,text="Select Date",command=fetch_date, bg="black", fg='white')
but.pack()

date = tk.Label(frame, text="")
date.pack()

# quit button 
quit = tk.Button(frame, text="Quit", command=frame.destroy)
quit.pack()

# main loop
frame.mainloop()
