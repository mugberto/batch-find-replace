from os import scandir
from os.path import isfile


def get_files(path):
    try:
        if path == "":
            path = "."
        return [file.path for file in scandir(path) if isfile(file.path)]
    except FileNotFoundError:
        print("Input a correct path")
