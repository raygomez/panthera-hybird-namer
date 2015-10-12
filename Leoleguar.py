from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Leoleguar(Panthera):
    def __init__(self, gender=random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Leoleguar'

    def getFemaleName(self):
        return 'Leoleguaress'

    def getOffspring(self, other):
        if isinstance(other, Leoleguar):
            return Leoleguar()

        Panthera.getOffspring(self, other)
