from __future__ import print_function
from Panthera import Panthera
import random

__author__ = 'ragomez'

class Jagupard(Panthera):

    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 2

    def getMaleName(self):
        return 'Jagupard'

    def getFemaleName(self):
        return 'Jagupardess'

    def getOffspring(self, other):
        if isinstance(other, Jagupard):
            return Jagupard()

        Panthera.getOffspring(self,other)

