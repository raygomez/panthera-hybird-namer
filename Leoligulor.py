from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Leoligulor(Panthera):
    def __init__(self, gender=random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Leoligulor'

    def getFemaleName(self):
        return 'Leoligulor'

    def getOffspring(self, other):
        if isinstance(other, Leoligulor):
            return Leoligulor()

        Panthera.getOffspring(self, other)
