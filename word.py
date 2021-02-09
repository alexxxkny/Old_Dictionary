class Word:
    def __init__(self, original, translate, topic, kind):
        self.original = original
        self.translate = translate
        self.topic = topic
        self.kind = kind

    def __str__(self):
        return self.original + ' = ' + ', '.join(self.translate) + '\t(' + self.topic + ', ' + self.kind + ')'

    def make_dict_to_json(self):
        return {'original': self.original, 'translate': list(self.translate), 'topic': self.topic, 'kind': self.kind}

    def check_translate(self, translate):
        if translate in self.translate:
            return True
        else:
            return False
