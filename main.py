import json
import dictionary
import console_menu
from word import Word


words = dictionary.load_word_list_from_file('words.txt')
console_menu.menu()
while True:
    inp = input('Select action: ')
    while not inp.isnumeric():
        inp = input('Yot have to enter a number.\nTry again: ')
    choice = int(inp)
    if choice == 0:
        break
    elif choice == 1:
        console_menu.show_word_list(words)
    elif choice == 2:
        new_word = console_menu.enter_word()
        words.append(new_word)
    elif choice == 3:
        console_menu.delete_word(words)
    elif choice == 4:
        print('Choose mode.\n1 - en -> ru\n2 - ru -> en')
        lang = 'en'
        while True:
            answer = input('Mode: ').strip()
            if answer == '1':
                #lang = 'en'
                break
            elif answer == '2':
                lang = 'ru'
                break
            else:
                print('Incorrect input. Try again.')
        right = console_menu.test_list(words, lang=lang)
        print('Result: ', right, '/', len(words), sep='')
    else:
        print('Fucking asshole')
dictionary.save_word_list_to_file(words, 'words.txt')