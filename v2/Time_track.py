

class Time_track:
    
    def __init__(self, start_time, end_time, duration, topic):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.topic = topic

    def __str__(self):
        return f"Start time:{self.start_time} # End time:{self.end_time} # Duration:{self.duration} # Topic:{self.topic}"

    def save_data():
        print("save data")


    def change_start_time(self, new_start_time):
        self.start_time = new_start_time
        print("change start time")


    def change_end_time(self, new_end_time):
        self.end_time = new_end_time
        print("change end time")