import json
from word import Word


codec = 'utf-8'
indent = 4
ensure_ascii = False


def save_word_list_to_file(words, filename):
    dir_list = [word.make_dict_to_json() for word in words]
    with open(filename, 'w', encoding=codec) as file:
        json.dump(dir_list, file, ensure_ascii=ensure_ascii, indent=indent)


def load_word_list_from_file(filename):
    with open(filename, 'r', encoding=codec) as file:
        data = json.load(file)
    return [Word(word['original'], set(word['translate']), word['topic'], word['kind']) for word in data]


def save_list_to_file_json(data, filename):
    with open(filename, 'w', encoding=codec) as file:
        json.dump(data, file, ensure_ascii=ensure_ascii, indent=indent)


def load_list_from_file_json(filename):
    with open(filename, 'r', encoding=codec) as file:
        data = json.load(file)
    return data
