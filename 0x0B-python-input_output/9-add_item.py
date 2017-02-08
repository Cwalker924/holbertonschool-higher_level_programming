#!/usr/bin/python3
from sys import argv


save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file


if __name__ == "__main__":
    try:
        jlist = load_from_json_file("add_item.json")
    except:
        jlist = []
    for argc in argv[1:]:
        jlist.append(argc)
    save_to_json_file(jlist, "add_item.json")
