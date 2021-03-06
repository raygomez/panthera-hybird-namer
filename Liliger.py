from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'

class Liliger(Panthera):

    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Liliger'

    def getFemaleName(self):
        return 'Liligress'

    def getOffspring(self, other):
        if isinstance(other, Liliger):
            return Liliger()

        Panthera.getOffspring(self,other)

