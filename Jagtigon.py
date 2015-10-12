from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'


class Jagtigon(Panthera):

    def __init__(self, gender=random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 3

    def getMaleName(self):
        return 'Jagtigon'

    def getFemaleName(self):
        return 'Jagtigoness'

    def getOffspring(self, other):
        if isinstance(other, Jagtigon):
            return Jagtigon()

        Panthera.getOffspring(self, other)
