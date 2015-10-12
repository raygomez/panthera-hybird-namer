from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Tiliguar(Panthera):
    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Tiliguar'

    def getFemaleName(self):
        return 'Tiliguaress'

    def getOffspring(self, other):
        if isinstance(other, Tiliguar):
            return Tiliguar()

        Panthera.getOffspring(self, other)
