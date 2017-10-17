class Allergies(object):
    allergies_list = ['cats', 'pollen', 'chocolate', 'tomatoes', 'strawberries', 'shellfish', 'peanuts', 'eggs']

    def __init__(self, score):
        self._score = score
        self._bin = '{0:08b}'.format(score % 256)
        self._lst = [x for x, y in zip(self.allergies_list, self._bin) if y == '1']

    def is_allergic_to(self, item):
        return item in self._lst

    @property
    def lst(self):
        return self._lst
