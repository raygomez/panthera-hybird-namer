from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'

class Lijagupard(Panthera):

    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Lijagupard'

    def getFemaleName(self):
        return 'Lijagupardess'

    def getOffspring(self, other):
        if isinstance(other, Lijagupard):
            return Lijagupard()

        Panthera.getOffspring(self,other)

