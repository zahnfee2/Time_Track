from include import csv_path
import os.path
import csv

def write_in_file(filename, content, operator):
    with open(filename, operator) as f:
        f.write(content)


def get_content_of_file(filename):
    with open(filename, 'w') as f:
        content = f.read()
    return content


def write_in_csv_file(row):
    f = open(csv_path, 'a')
    writer = csv.writer(f)
    if(os.path.isfile(csv_path)):
        first_line = ['start', 'end', 'duration', 'topic']
        writer.writerow(first_line)
    writer.writerow(row)


