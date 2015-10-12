from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Lipard(Panthera):
    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 2

    def getMaleName(self):
        return 'Lipard'

    def getFemaleName(self):
        return 'Lipardess'

    def getOffspring(self, other):
        if isinstance(other, Lipard):
            return Lipard()

        Panthera.getOffspring(self, other)
