class Word:
    def __init__(self, original='', translate=set()):
        self.original = original
        self.translate = translate

    def __str__(self):
        return self.original + ' = ' + ', '.join(self.translate)

    def make_dict_to_json(self):
        return {'original': self.original, 'translate': list(self.translate)}

    def check_translate(self, translate):
        if translate in self.translate:
            return True
        else:
            return False
