from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Jagliguar(Panthera):

    def __init__(self, gender=random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Jagliguar'

    def getFemaleName(self):
        return 'Jagliguaress'

    def getOffspring(self, other):
        if isinstance(other, Jagliguar):
            return Jagliguar()

        Panthera.getOffspring(self, other)
