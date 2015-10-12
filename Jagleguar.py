from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Jagleguar(Panthera):

    def __init__(self, gender=random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Jagleguar'

    def getFemaleName(self):
        return 'Jagleguaress'

    def getOffspring(self, other):
        if isinstance(other, Jagleguar):
            return Jagleguar()

        Panthera.getOffspring(self, other)
