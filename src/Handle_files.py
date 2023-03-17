#from include import csv_path, connect_csv_with_git
import include as inc
from os.path import exists
import os
import git
import pandas as pd
import csv

def create_file_if_not_exists(): 
    if not exists(inc.csv_path):
        first_line = ['date', 'start', 'end', 'duration', 'topic']
        with open(inc.csv_path, 'w', encoding='UTF8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(first_line)

def write_in_csv_file(row):
    with open(inc.csv_path, 'a', encoding='UTF8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(row)

def get_content_csv_file(filename):
    content = pd.read_csv(filename, sep=';')
    content = pd.DataFrame(content)
    return content

def write_List_in_csv(filename, content):
    content.to_csv(filename, index=False, sep=';')

def pull_tracked_time():
    if inc.connect_csv_with_git:
        path = os.getcwd() + "/time_track_data"
        repo = git.Repo(path)
        repo.git.pull()
        print("Get data from git.")

def push_tracked_time():
    if inc.connect_csv_with_git:
        path = os.getcwd() + "/time_track_data"
        repo = git.Repo(path)
        count_modified_files = len(repo.index.diff(None))
        if count_modified_files > 0:
            repo.git.add("tracked_time.csv")
            repo.git.commit(m = "change tracked_time.csv")
            repo.git.push()
            print("Pushed data to git.")
