import json
from word import Word


def save_word_list_to_file(words, filename):
    dir_list = [word.make_dict_to_json() for word in words]
    with open(filename, 'w') as file:
        json.dump(dir_list, file)


def load_word_list_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return [Word(word['original'], set(word['translate'])) for word in data]


def save_list_to_file_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_list_from_file_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
