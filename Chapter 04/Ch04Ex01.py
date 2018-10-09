from os import listdir
from os.path import join
import sys

DATA_DIRECTORY = 'data'
FILE_EXTENSION = '.lst'
PROMPT = "[A]dd [D]elete [S]ave [Q]uit:"
ERROR_STR = "ERROR: Invalid choice -- enter one of 'AaDdSsQq'.\n" \
            "Press Enter to continue..."
ADD, DELETE, SAVE, QUIT = range(4)
ACTIONS = {
        'A': ADD,
        'D': DELETE,
        'S': SAVE,
        'Q': QUIT,
}


def get_file_names_from_dir(directory, extension):
    f_names = [f for f in listdir(directory) if f.endswith(extension)]
    return [join(directory, f_name) for f_name in f_names]


def display_files(file_names):
    options = ["Choose a file to load or enter 0 to create a new one:"]
    for i, f_name in enumerate(file_names):
        options.append("{} - {}".format(i + 1, f_name))
    while True:
        try:
            selection = int(input('\n'.join(options) + '\n'))
        except ValueError:
            print("Please enter an integer.")
            continue
        if 0 < selection < len(options):
            return f_name
        elif selection == 0:
            return input("Enter new file name: ")


def files_switch(directory, extension):
    existing_files = get_file_names_from_dir(directory, extension)
    chosen_filename = display_files(existing_files)
    return chosen_filename


def sort_items(items):
    """ Case-insensitive sort of titles. """
    items.sort(key=lambda s: s.lower())


def get_action():
    while True:
        option = input(PROMPT)
        try:
            action = ACTIONS[option.upper()]
            return action
        except KeyError:
            input(ERROR_STR)


def get_items(filename):
    with open(DATA_DIRECTORY + filename, 'r') as f:
        items = f.read().strip('\n').splitlines()
    return sorted(items, key=lambda s: s.lower())


def main():
    chosen_filename = files_switch(DATA_DIRECTORY, FILE_EXTENSION)
    items = get_items(chosen_filename)
    while True:
        action = get_action()
        if action == ADD:
            pass
        elif action == DELETE:
            pass
        elif action == SAVE:
            pass
        elif action == QUIT:
            sys.exit(0)
        else:
            raise NotImplementedError("Something went wrong")


main()
