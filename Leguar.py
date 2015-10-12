from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'

class Leguar(Panthera):

    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 2

    def getMaleName(self):
        return 'Leguar'

    def getFemaleName(self):
        return 'Leguaress'

    def getOffspring(self, other):
        if isinstance(other, Leguar):
            return Leguar()

        Panthera.getOffspring(self,other)

