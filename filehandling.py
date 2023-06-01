from os import path
from json import dump, load

FILE_NAME = 'notes_db.json'


def store_notes(dictionary):
    with open(FILE_NAME, 'w') as file:
        dump(dictionary, file)


def read_notes():  # Считывание
    if not path.exists(FILE_NAME):
        dictionary = dict()
    else:
        with open(FILE_NAME, 'r') as file:
            dictionary = load(file)
    return dictionary
