#!/usr/bin/python3
from json import load

def load_from_json_file(filename):
    with open(filename) as file:
        return (load(file))
