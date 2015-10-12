from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Tileguar(Panthera):
    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Tileguar'

    def getFemaleName(self):
        return 'Tileguaress'

    def getOffspring(self, other):
        if isinstance(other, Tileguar):
            return Tileguar()

        Panthera.getOffspring(self, other)
