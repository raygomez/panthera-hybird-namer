from __future__ import print_function
import random

from Panthera import Panthera

__author__ = 'ragomez'


class Liger(Panthera):

    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 2

    def getMaleName(self):
        return 'Liger'

    def getFemaleName(self):
        return 'Ligress'

    def getOffspring(self, other):
        if isinstance(other, Liger):
            return Liger()
        Panthera.getOffspring(self,other)
