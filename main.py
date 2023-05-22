from libs.utils import get_files


def main():
    print(
        "This script finds a string of characters in a batch of files\nand replace it with a new one"
    )
    files = get_files(input("Enter folder's location: ").strip())
    old_string = input("Enter the characters to be replaced: ")
    new_string = input("Enter the characters to replace with: ")
    for file in files:
        txt = ""
        with open(file, "rt") as f:
            txt = f.read()
            txt = txt.replace(old_string, new_string)
        with open(file, "wt") as f:
            f.write(txt)


if __name__ == "__main__":
    main()
