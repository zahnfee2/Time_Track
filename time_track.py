import tkinter as tk
from datetime import datetime

counter = 0

# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('200x100')

def track():
    time_stamp = datetime.now()
    f = open("work_time.csv", "a")
    text = str(time_stamp) + ';'
    f.write(text)
    global counter 
    counter = counter + 1
    if counter % 2 == 1:
        print("Start")
        btn['text'] = 'End'
    else:
        print("End")
        f.write('\n')
        btn['text'] = 'Start'

    f.close()

# Start Button
btn = tk.Button(frame, text = "Start", command = track)
btn.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
