from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Leoliguar(Panthera):
    def __init__(self, gender=random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Leoliguar'

    def getFemaleName(self):
        return 'Leoliguaress'

    def getOffspring(self, other):
        if isinstance(other, Leoliguar):
            return Leoliguar()

        Panthera.getOffspring(self, other)
