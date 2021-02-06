from word import Word

original = input('Enter the word: ')
translate = input('Enter the translates separated by comma: ')
translates = [word.strip() for word in translate.split(',')]

example = Word(original, translates)
dir(list)
print(example)