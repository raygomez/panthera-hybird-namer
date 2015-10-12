from __future__ import print_function
from Panthera import Panthera

__author__ = 'raygomez'


class Jaguar(Panthera):

    def getMaleName(self):
        return 'Jaguar'

    def getFemaleName(self):
        return 'Jaguaress'

    def getOffspring(self, other):
        if isinstance(other, Jaguar):
            return Jaguar()

