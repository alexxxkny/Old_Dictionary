class Word:
    def __init__(self, original='', translate=[]):
        self.__original = original
        self.__translate = translate

    def __str__(self):
        return self.__original + ' = ' + ', '.join(self.__translate)
