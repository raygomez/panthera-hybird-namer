from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'

class Leoger(Panthera):

    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 2

    def getMaleName(self):
        return 'Leoger'

    def getFemaleName(self):
        return 'Leogress'

    def getOffspring(self, other):
        if isinstance(other, Leoger):
            return Leoger()

        Panthera.getOffspring(self,other)

