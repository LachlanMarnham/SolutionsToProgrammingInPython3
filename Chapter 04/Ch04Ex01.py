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
ACTION_TO_PROMPT = {
    ADD: 'Add item: ',
    DELETE: 'Delete item number (or 0 to cancel): ',
    SAVE: 'Press Enter to continue... ',
    QUIT: 'Save unsaved changes? (y/n): ',
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
            return file_names[selection - 1]
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
    with open(filename, 'r') as f:
        items = f.read().strip('\n').splitlines()
    return sorted(items, key=lambda s: s.lower())


def add_new_item(items):
    new_item = input(ACTION_TO_PROMPT[ADD])
    items.append(new_item)
    sort_items(items)
    return items


def delete_item(items):
    index_to_delete = int(input(ACTION_TO_PROMPT[DELETE])) - 1
    if not index_to_delete + 1:
        return
    else:
        try:
            items.pop(index_to_delete)
        except IndexError:
            print('Invalid index.')


def save_items(items, filename):
    with open(filename, 'w') as f:
        f.write('\n'.join(items))


def check_save_and_quit(items, filename, unsaved_changes):
    action = input(ACTION_TO_PROMPT[QUIT])
    if action.lower() != 'n' and unsaved_changes:
        save_items(items, filename)
    sys.exit(0)


def main():
    chosen_filename = files_switch(DATA_DIRECTORY, FILE_EXTENSION)
    items = get_items(chosen_filename)
    unsaved_changes_flag = False
    while True:
        if len(items) == 0:
            print('-- no items are in the list --')
        else:
            item_display = ''
            for i, item in enumerate(items):
                item_display += "\n{}: {}".format(i + 1, item)
            print(item_display)
        action = get_action()
        if action == ADD:
            add_new_item(items)
            unsaved_changes_flag = True
        elif action == DELETE:
            delete_item(items)
            unsaved_changes_flag = True
        elif action == SAVE:
            save_items(items, chosen_filename)
            unsaved_changes_flag = False
        elif action == QUIT:
            check_save_and_quit(items, chosen_filename, unsaved_changes_flag)


main()
