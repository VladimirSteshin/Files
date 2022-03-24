import os

file_path_merge = os.path.join(os.getcwd(), 'For merge')

with os.scandir(file_path_merge) as objects:
    file_list = []
    for file in objects:
        if 'txt' in file.name:
            file_list.append(file.name)


def file_sort(library):
    file_dict = {}
    for doc in library:
        with open(doc, encoding='UTF-8') as content:
            file_dict[doc] = content.read().strip()
    return file_dict

