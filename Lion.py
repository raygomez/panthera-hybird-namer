from __future__ import print_function
from Panthera import Panthera
from Tiger import Tiger

__author__ = 'raygomez'


class Liger(Panthera):

    def __init__(self):
        Panthera.__init__(self)
        self.generation = 2

    def getMaleName(self):
        return 'Liger'

    def getFemaleName(self):
        return 'Ligress'

    def getOffspring(self, other):
        if isinstance(other, Liger):
            return Liger()


class Lion(Panthera):

    def getMaleName(self):
        return 'Lion'

    def getFemaleName(self):
        return 'Lioness'

    def getOffspring(self, other):
        if isinstance(other, Lion):
            return Lion()

        elif isinstance(other, Tiger):
            if self.isMale():
                return Liger()

        Panthera.getOffspring(self, other)


