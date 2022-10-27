from include import csv_path
from os.path import exists
import csv

def write_in_file(filename, content, operator):
    with open(filename, operator) as f:
        f.write(content)


def get_content_of_file(filename):
    with open(filename, 'w') as f:
        content = f.read()
    return content


def write_in_csv_file(row):

    if not exists(csv_path):
        first_line = ['start', 'end', 'duration', 'topic']
        with open(csv_path, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(first_line)

    with open(csv_path, 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(row)


