from include import csv_path
from os.path import exists
import os
import git
import pandas as pd
import csv

#def write_in_file(filename, content, operator):
#    with open(filename, operator) as f:
#        f.write(content)


#def get_content_of_file(filename):
#    with open(filename, 'w') as f:
#        content = f.read()
#    return content


def write_in_csv_file(row):
    if not exists(csv_path):
        first_line = ['start', 'end', 'duration', 'topic']
        with open(csv_path, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(first_line)

    with open(csv_path, 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(row)

    push_tracked_time()


def get_content_csv_file(filename):
    pull_tracked_time()
    content = pd.read_csv(filename)
    content = pd.DataFrame(content)
    return content


def write_List_in_csv(filename, content):
    print(filename)
    content.to_csv(filename, index=False, sep=',')
    push_tracked_time()


def pull_tracked_time():
    path = os.getcwd() + "/time_track_data"
    repo = git.Repo(path)
    repo.git.pull()

def push_tracked_time():
    path = os.getcwd() + "/time_track_data"
    repo = git.Repo(path)
    pull_tracked_time()
    repo.git.add("tracked_time.csv")
    repo.git.commit(m = "add new line tracked_time.csv")
    repo.git.push()
    print("Pushed to Github done.")
