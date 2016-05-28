import os


# Each website you crawl is a seprate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.mkdir(directory)


# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a', encoding='utf-8', errors='ignore') as f:
        f.write(data + '\n')


# Delete the contents of a file
def delete_files_contents(path):
    with open(path, 'w'):
        pass


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt', encoding='utf-8', errors='ignore') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# Iterate thrrough a set, each item will be a new line in the file
def set_to_file(links, file):
    delete_files_contents(file)
    for link in sorted(links):
        append_to_file(file, link)