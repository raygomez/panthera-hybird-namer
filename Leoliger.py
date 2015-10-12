from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Leoliger(Panthera):
    def __init__(self, gender=random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Leoliger'

    def getFemaleName(self):
        return 'Leoligress'

    def getOffspring(self, other):
        if isinstance(other, Leoliger):
            return Leoliger()

        Panthera.getOffspring(self, other)
