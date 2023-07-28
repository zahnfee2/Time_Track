from datetime import datetime
from include import *
import pandas as pd
from os.path import exists
import os
from Handle_files import write_List_in_csv , get_content_csv_file

path = os.getcwd()


def check_datetime_format(datetime_str):
        try:
            datetime.strptime(datetime_str, time_format)
            return True
        except ValueError:
            return False


def sort_Content(content): 
    # Convert To Datetime 
    content['date'] = pd.to_datetime(content.date)
    content['start'] = pd.to_datetime(content.start)
    content['end'] = pd.to_datetime(content.end)

    # Sort 
    content.sort_values(by='date', inplace=True)

    # Change Format 
    content['date'] = content['date'].dt.strftime(date_format)
    content['start'] = content['start'].dt.strftime(time_format)
    content['end'] = content['end'].dt.strftime(time_format)
    return content


def get_entire_duration():
    if exists(csv_path):
        content = pd.read_csv(csv_path, sep=";")
        content = pd.DataFrame(content)
        content['duration'] = pd.to_timedelta(content.duration)
        td = content.duration.sum()
        total_seconds = td.total_seconds()                # Convert timedelta into seconds
        seconds_in_hour = 60 * 60                         # Set the number of seconds in an hour
        td_in_hours = total_seconds / seconds_in_hour     # Convert timedelta into hours
        return round(td_in_hours, 2)
    else: 
        return 0

def delete_new_Line(string):
    string = string.replace('\n',' ')
    return string

def check_If_gitrepo_exists(): 
    git_path = str(os.path.dirname(csv_path)) + "/.git"
    return os.path.exists(git_path)


def check_overlap(timerow): 
    content = get_content_csv_file(csv_path)
    content['start'] = pd.to_datetime(content.start, infer_datetime_format = True)
    content['end'] = pd.to_datetime(content.end, infer_datetime_format = True)
    row_start = pd.to_datetime(timerow[0], infer_datetime_format = True)
    row_end = pd.to_datetime(timerow[1], infer_datetime_format = True)
    for i in range(0,len(content)):
        if row_start > content['start'][i] and row_start < content['end'][i]: 
            return True
        elif row_end > content['start'][i] and row_end < content['end'][i]:
            return True
    
    return False
