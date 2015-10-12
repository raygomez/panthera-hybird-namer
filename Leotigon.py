from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Leotigon(Panthera):
    def __init__(self, gender=random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Leotigon'

    def getFemaleName(self):
        return 'Leotigoness'

    def getOffspring(self, other):
        if isinstance(other, Leotigon):
            return Leotigon()

        Panthera.getOffspring(self, other)
