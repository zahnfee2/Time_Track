from datetime import datetime
from include import *
import pandas as pd
from os.path import exists
#from git import Repo
import git
import os
from Handle_files import write_List_in_csv

path = os.getcwd()

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




def change_end_content(start_str, end_str, duration_str, topic_str):
    start = []
    end = []
    duration = []
    topic = []

    start = create_list(start_str)
    end = create_list(end_str)
    duration = create_list(duration_str)
    topic = create_list(topic_str)

    content = {'start': start, 'end': end, 'duration': duration, 'topic': topic}
    content = pd.DataFrame(content)

    content = delete_last_entry_of_df_if_empty(content)

    write_List_in_csv(csv_path, content)

def delete_last_entry_of_df_if_empty(content):
    if(not content.start[len(content)-1]):
        content.drop(index=content.index[-1],axis=0,inplace=True)
    return content


def create_list(stri):
    out = []
    buff = []
    for line in stri:
        if line == '\n':
            out.append(''.join(buff))
            buff = []
        else:
            buff.append(line)

    return out


def push_tracked_time():
    path = os.getcwd() + "/time_track_data"
    repo = git.Repo(path)
    repo.git.pull()
    repo.git.add("tracked_time.csv")
    repo.git.commit(m = "add new line tracked_time.csv")
    repo.git.push()
    print("Pushed to Github done.")