from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'

class Liliguar(Panthera):

    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Liliguar'

    def getFemaleName(self):
        return 'Liliguaress'

    def getOffspring(self, other):
        if isinstance(other, Liliguar):
            return Liliguar()

        Panthera.getOffspring(self,other)

