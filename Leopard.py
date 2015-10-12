from __future__ import print_function
from Panthera import Panthera

__author__ = 'raygomez'


class Leopard(Panthera):
    def getMaleName(self):
        return 'Leopard'

    def getFemaleName(self):
        return 'Leopardess'

    def getOffspring(self, other):
        if isinstance(other, Leopard):
            return Leopard()
