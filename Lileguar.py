from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'

class Lileguar(Panthera):

    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Lileguar'

    def getFemaleName(self):
        return 'Lileguaress'

    def getOffspring(self, other):
        if isinstance(other, Lileguar):
            return Lileguar()

        Panthera.getOffspring(self,other)

