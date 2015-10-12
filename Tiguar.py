from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Tiguar(Panthera):
    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 2

    def getMaleName(self):
        return 'Tiguar'

    def getFemaleName(self):
        return 'Tiguaress'

    def getOffspring(self, other):
        if isinstance(other, Tiguar):
            return Tiguar()

        Panthera.getOffspring(self, other)
