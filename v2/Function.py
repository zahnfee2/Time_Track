from datetime import datetime
from include import *
import pandas as pd
from os.path import exists

def check_datetime_format(datetime_str):
        try:
            datetime.strptime(datetime_str, time_format)
            return True
        except ValueError:
            return False


def sort_Content(content): 
    content['start'] = pd.to_datetime(content.start, infer_datetime_format = True)
    content.sort_values(by='start', ascending=True, inplace=True)
    return content


def append_Line(content, line):
    print(content, " Line ", line)
    content.append(line, ignore_index=True)
    return content

def get_entire_duration():
    if(exists(csv_path)):
        content = pd.read_csv(csv_path)
        content = pd.DataFrame(content)
        content['duration'] = pd.to_timedelta(content.duration)
        return content.duration.sum()
    else: 
        return 0

def delete_new_Line(string):
    string = string.replace('\n',' ')
    return string