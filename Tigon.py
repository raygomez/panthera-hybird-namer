from __future__ import print_function
from Panthera import Panthera

__author__ = 'ragomez'


class Tigon(Panthera):
    def __init__(self):
        Panthera.__init__(self)
        self.generation = 2

    def getMaleName(self):
        return 'Tigon'

    def getFemaleName(self):
        return 'Tigoness'

    def getOffspring(self, other):
        if isinstance(other, Tigon):
            return Tigon()

        Panthera.getOffspring(self, other)
