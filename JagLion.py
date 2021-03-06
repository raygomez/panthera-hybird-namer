from __future__ import print_function
import random

from Panthera import Panthera

__author__ = 'ragomez'


class Jaglion(Panthera):

    def __init__(self, gender=random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 2

    def getMaleName(self):
        return 'Jaglion'

    def getFemaleName(self):
        return 'Jaglioness'

    def getOffspring(self, other):
        if isinstance(other, Jaglion):
            return Jaglion()

        Panthera.getOffspring(self, other)
