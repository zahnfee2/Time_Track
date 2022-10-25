
def write_in_file(filename, content, operator):
    with open(filename, operator) as f:
        f.write(content)


def get_content_of_file(filename):
    with open(filename, 'w') as f:
        content = f.read()
