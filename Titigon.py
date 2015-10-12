from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Titigon(Panthera):
    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Titigon'

    def getFemaleName(self):
        return 'Titigoness'

    def getOffspring(self, other):
        if isinstance(other, Titigon):
            return Titigon()

        Panthera.getOffspring(self, other)
