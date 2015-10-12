from __future__ import print_function
import random

from Panthera import Panthera

__author__ = 'ragomez'


class Tigard(Panthera):

    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 2

    def getMaleName(self):
        return 'Tigard'

    def getFemaleName(self):
        return 'Tigardess'

    def getOffspring(self, other):
        if isinstance(other, Tigard):
            return Tigard()
        Panthera.getOffspring(self,other)
