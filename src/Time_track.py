class Time_track:
    
    def __init__(self, start_time):
        self.start_time = start_time

    def __str__(self):
        return f"Start time: {self.start_time}"

    def add_endtime(self, end_time):
        self.end_time = end_time

    def add_duration(self, duration):
        self.duration = duration

    def add_topic(self, topic):
        self.topic = topic

    def save_data():
        print("save data")

    def change_start_time(self, new_start_time):
        self.start_time = new_start_time
        print("change start time")

    def change_end_time(self, new_end_time):
        self.end_time = new_end_time
        print("change end time")