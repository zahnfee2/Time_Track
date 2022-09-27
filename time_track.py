import tkinter as tk
from datetime import datetime
from os.path import exists

# Counter to identify start and end
counter = 0
start_time = datetime.now()

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('200x100')

# write the timestamp in a file
def track():

    # create timestamp
    time_stamp = datetime.now()

    filename = "working_time.csv"
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


# show label while the time is recording
lab = tk.Label(frame, text="time is running ...")

# Start/End Button
btn = tk.Button(frame, text = "Start", command = track)
btn.pack()

# quit button 
quit = tk.Button(frame, text="Quit", command=frame.destroy)
quit.pack()

# main loop
frame.mainloop()
