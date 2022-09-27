import tkinter as tk
from datetime import datetime
from os.path import exists
from tkcalendar import Calendar
from tktimepicker import AnalogPicker, AnalogThemes

# Counter to identify start and end
counter = 0
start_time = datetime.now()

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('600x800')

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



# save date time in file 
def save_datetime(date, time):
    print(date + " ## " + time)



######## Start / End Button ########

# show label while the time is recording
lab = tk.Label(frame, text="time is running ...")

# Start/End Button
btn = tk.Button(frame, text = "Start", command = track)
btn.pack()


######## Calendar picker ########

# gettin date from the calendar
def fetch_date():
    date_lbl.config(text = "Selected Date is: " + str(tkc.get_date()))

tkc = Calendar(frame,selectmode = "day",year=2022,month=10,date=1)
tkc.pack()
but = tk.Button(frame,text="Select Date",command=fetch_date, bg="black", fg='white')
but.pack()

# conver time to a string
date = str(tkc.get_date())

# create date label 
date_lbl = tk.Label(frame, text="")
date_lbl.pack()

######## Time picker ########
time_picker = AnalogPicker(frame)
time_picker.pack(expand=True, fill="both")

theme = AnalogThemes(time_picker)
theme.setDracula()
time = str(time_picker.hours) + ':' + str(time_picker.minutes)

######## Save Button ########
save = tk.Button(frame, text="Save", command=save_datetime(date ,time))
save.pack()

# quit button 
quit = tk.Button(frame, text="Quit", command=frame.destroy)
quit.pack()

# main loop
frame.mainloop()
