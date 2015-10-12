from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Tiliger(Panthera):
    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Tiliger'

    def getFemaleName(self):
        return 'Tiligress'

    def getOffspring(self, other):
        if isinstance(other, Tiliger):
            return Tiliger()

        Panthera.getOffspring(self, other)
