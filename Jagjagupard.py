from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Jagjagupard(Panthera):

    def __init__(self, gender=random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Jagjagupard'

    def getFemaleName(self):
        return 'Jagjagupardess'

    def getOffspring(self, other):
        if isinstance(other, Jagjagupard):
            return Jagjagupard()

        Panthera.getOffspring(self, other)
