from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Leojagupard(Panthera):
    def __init__(self, gender=random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Leojagupard'

    def getFemaleName(self):
        return 'Leojagupardess'

    def getOffspring(self, other):
        if isinstance(other, Leojagupard):
            return Leojagupard()

        Panthera.getOffspring(self, other)
