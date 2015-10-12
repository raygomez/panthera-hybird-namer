from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'

class Lililiger(Panthera):

    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 4

    def getMaleName(self):
        return 'Li-liliger'

    def getFemaleName(self):
        return 'Li-liligress'

    def getOffspring(self, other):
        if isinstance(other, Lililiger):
            return Lililiger()

        Panthera.getOffspring(self,other)

