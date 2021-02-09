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
    # topic = input('Enter topic: ')
    # kind = input('Enter class of word: ')
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


def test_en_ru(word):
    remaining_translates = word.translate
    n = len(remaining_translates)
    print(word.original)
    while True:
        answer = input('Enter translate: ')
        if answer == '->':
            print(word)
            return False
        answer_set = {word.strip() for word in answer.split(',')}
        remaining_translates = remaining_translates - answer_set
        right_word_count = n - len(remaining_translates)
        if right_word_count == n:
            print('right')
            return True
        else:
            print(right_word_count, '/', n, sep='')


def test_ru_en(word):
    print(','.join(word.translate))
    while True:
        answer = input('Enter translate: ')
        if answer == '->':
            print(word)
            return False
        elif answer == word.original:
            print('right')
            return True
        else:
            print('Wrong. Try again.')


def test_list(words, lang='en', random_order=False):
    if random_order is True:
        shuffle(words)
    right = 0
    if lang == 'en':
        for word in words:
            result = test_en_ru(word)
            if result is True:
                right += 1
    elif lang == 'ru':
        for word in words:
            result = test_ru_en(word)
            if result is True:
                right += 1
    return right







