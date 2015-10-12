from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Tijagupard(Panthera):
    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Tijagupard'

    def getFemaleName(self):
        return 'Tijagupardess'

    def getOffspring(self, other):
        if isinstance(other, Tijagupard):
            return Tijagupard()

        Panthera.getOffspring(self, other)
