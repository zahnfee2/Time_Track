import tkinter as tk
from datetime import datetime

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

    # open file
    f = open("work_time.csv", "a")

    # create file content
    text = str(time_stamp) + ';'

    # write content in fiel
    f.write(text)

    # check if start or end
    global counter 
    counter = counter + 1
    if counter % 2 == 1:
        global start_time 
        start_time = time_stamp
        btn['text'] = 'End'
    else:
        # calculate the duration
        end_time = time_stamp
        duration = end_time - start_time

        # insert a new line in the file
        f.write(str(duration) + '\n')
        btn['text'] = 'Start'

    f.close()

# Start/End Button
btn = tk.Button(frame, text = "Start", command = track)
btn.pack()

# main loop
frame.mainloop()
