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
    original = input('Enter the word: ').strip()
    translate = input('Enter the translates separated by comma: ')
    topic = input('Enter topic: ').strip()
    kind = input('Enter class of word: ').strip()
    translates = {word.strip() for word in translate.split(',')}
    return Word(original, translates, topic, kind)


def show_word_list(words):
    for i in range(len(words)):
        print("#" + str(i + 1) + '\t' + str(words[i]))


def delete_word(words):
    num = int(input('Enter word number to delete: '))
    while not (0 < num <= len(words)):
        num = int(input('There is not such number here.\nTry again: '))
    del words[num - 1]


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


def get_test_settings(words, topics, kinds):
    # random_order = False
    # count = 0
    # topic = 'all'
    # kind = 'all'
    while True:
        random_order = input('Random order (y/n): ').strip()
        if random_order == 'y':
            random_order = True
            break
        elif random_order == 'n':
            random_order = False
            break
        else:
            print('Wrong input. Try again.')
    while True:
        count = input('Enter word count: ').strip()
        if count.isnumeric() is not True:
            print('Enter number, please.')
            continue
        count = int(count)
        if count <= 0:
            print('stupid?')
            continue
        elif count > len(words):
            print('There are not so many words. Try less.')
            continue
        else:
            break
    while True:
        topic = input('Enter topic name: ').strip()
        if topic not in topics:
            pass # HEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRREEEEEEEEEEEEEEEEEEEEEE
    # check if exist
    kind = input('Enter word class: ').strip()
    return random_order, count, topic, kind


def make_list(words)





