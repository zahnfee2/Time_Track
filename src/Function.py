from datetime import datetime
from include import *
import pandas as pd
from os.path import exists
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
        content = pd.read_csv(csv_path, sep=";")
        content = pd.DataFrame(content)
        content['duration'] = pd.to_timedelta(content.duration)
        return content.duration.sum()
    else: 
        return 0

def delete_new_Line(string):
    string = string.replace('\n',' ')
    return string

def save_changed_content(content):
    start = []
    end = []
    duration = []
    topic = []
    content = list(content.split('\n'))
    for line in content:
        if not line:
            break
        line_list = list(line.split('\t' + '|' + '\t'))
        #print(line_list)
        if len(line_list) == 5:

            for i in range(0,len(line_list)):

                if i == 1:
                    start.append(line_list[i])
                elif i == 2:
                    end.append(line_list[i])
                elif i == 3:
                    duration.append(line_list[i])
                elif i == 4:
                    topic.append(line_list[i])
    
        else:
            print("To much entrys in Line ## line: " + str(len(line)))

    result = {'start': start, 'end': end, 'duration': duration, 'topic': topic}
    result = pd.DataFrame(result)
    write_List_in_csv(csv_path , result)
    

