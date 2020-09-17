b = 'paper'
t = 'title'


class Isomorphic_Strings():
    def __init__(self, word_1, word_2):
        self.word_1 = word_1
        self.word_2 = word_2

    def IsomoString(self):
        if len(self.word_1) == len(self.word_2):
            return self.word_2 == ''.join((dict(zip(self.word_1, self.word_2))[i] for i in self.word_1))
        return False


A = Isomorphic_Strings(b, t)
print(A.IsomoString())
