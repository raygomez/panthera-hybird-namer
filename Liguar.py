from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'

class Liguar(Panthera):

    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 2

    def getMaleName(self):
        return 'Liguar'

    def getFemaleName(self):
        return 'Liguaress'

    def getOffspring(self, other):
        if isinstance(other, Liguar):
            return Liguar()

        Panthera.getOffspring(self,other)

