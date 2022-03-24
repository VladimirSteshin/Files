import os

file_path = os.path.join(os.getcwd(), 'For merge')

with os.scandir(file_path) as objects:
    file_list = []
    for file in objects:
        if 'txt' in file.name and 'Re' not in file.name:
            file_list.append(file.name)
