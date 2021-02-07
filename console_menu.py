from word import Word
from random import shuffle


def menu():
    print('---MENU---')
    print('1 - show available words')
    print('2 - enter new word')
    print('3 - delete word')
    print('4 - test')
    print('0 - exit')


def enter_word():
    original = input('Enter the word: ')
    translate = input('Enter the translates separated by comma: ')
    translates = {word.strip() for word in translate.split(',')}
    return Word(original, translates)


def show_word_list(words):
    for i in range(len(words)):
        print("#" + str(i + 1) + '\t' + str(words[i]))


def delete_word(words):
    num = int(input('Enter word number to delete: '))
    while not (0 < num <= len(words)):
        num = int(input('There is not such number here.\nTry again: '))
    del words[num - 1]


def test(words, random_order=False):
    print('Test:\nWord count: ' + str(len(words)))
    number = 1
    if random_order is True:
        shuffle(words)
    for word in words:
        print('#' + str(number), word.original)
        number += 1
        answer = input('Enter translates separated by comma: ')
        if answer == 'stop':
            return
        answer_set = {word.strip() for word in answer.split(',')}
        if answer_set == word.translate:
            print('right')
        else:
            print('wrong')


