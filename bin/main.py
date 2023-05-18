from os import scandir
from os.path import isfile


def get_files(path):
    try:
        if path == "":
            path = "."
        return [file.path for file in scandir(path) if isfile(file.path)]
    except FileNotFoundError:
        print("Input a correct path")


def main():
    get_files(input("Enter folder's location: ").strip())
    files = get_files()
    old_string = input('Enter the characters to be replaced: ')
    new_string = input('Enter the characters to replace with: ')
    for file in files:
        txt =""
        with open(file, 'rt') as f:
            txt = f.read()
            txt = txt.replace(old_string, new_string)
        with open(file, 'wt') as f:
            f.write(txt)

if __name__ == "__main__":
    main()
