from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Jagliger(Panthera):

    def __init__(self, gender=random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Jagliger'

    def getFemaleName(self):
        return 'Jagligress'

    def getOffspring(self, other):
        if isinstance(other, Jagliger):
            return Jagliger()

        Panthera.getOffspring(self, other)
