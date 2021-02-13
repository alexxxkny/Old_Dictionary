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


def test_list(words, lang='en'):
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
        topic = input('Enter topic name: ').strip()
        if topic not in topics:
            print('There is no such topic in the list. Try again.')
            continue
        break
    while True:
        kind = input('Enter word class name: ').strip()
        if kind not in kinds:
            print('There is no such word class in the list. Try again.')
            continue
        break
    return random_order, topic, kind


def get_count(actual_len):
    if actual_len == 0:
        print('There are no such words.')
        return 0
    elif actual_len == 1:
        return 1
    else:
        print('There are', actual_len, 'such words.')
        while True:
            count = input('How many would you like to check: ').strip()
            if count.isnumeric() is False:
                print('Wrong input. Try again.')
                continue
            else:
                return int(count)


def make_list(words, random_order, topic, kind):
    working_list = [word for word in words if (word.topic == topic or topic == 'all')
                    and (word.kind == kind or kind == 'all')]
    if random_order is True:
        shuffle(working_list)
    count = get_count(len(working_list))
    if count == 0:
        return 0
    else:
        return working_list[:count]


def choose_mode():
    print('Choose mode.\n1 - en -> ru\n2 - ru -> en')
    while True:
        answer = input('Mode: ').strip()
        if answer == '1':
            return 'en'
        elif answer == '2':
            return 'ru'
        else:
            print('Incorrect input. Try again.')


def test(words, topics, kinds):
    random_order, topic, kind = get_test_settings(words, topics, kinds)
    working_list = make_list(words, random_order, topic, kind)
    lang = choose_mode()
    right = test_list(working_list, lang)
    return right / len(working_list)
