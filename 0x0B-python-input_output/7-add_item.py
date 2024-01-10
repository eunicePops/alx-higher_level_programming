#!/usr/bin/python3
""" script that adds all arguments to a Python list, and then save them to a file"""

import sys
import json
from os.path import exists
from save_to_json_file.py import save_to_json_file
from load_from_json_file.py import load_from_json_file

def add_to_list_and_save(args):
    # File name for storing the list as JSON
    file_name = "add_item.json"

    # Load existing list from the file or create a new one
    my_list = load_from_json_file(file_name) if exists(file_name) else []

    # Add command-line arguments to the list
    my_list.extend(args[1:])

    # Save the updated list to the file
    save_to_json_file(my_list, file_name)

if __name__ == "__main__":
    # Pass command-line arguments to the function
    add_to_list_and_save(sys.argv)


