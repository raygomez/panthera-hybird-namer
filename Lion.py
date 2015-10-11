from __future__ import print_function
from Panthera import Panthera

__author__ = 'raygomez'


class Lion(Panthera):

    def getMaleName(self):
        return 'Lion'

    def getFemaleName(self):
        return 'Lioness'

    def getOffspring(self, other):
        if isinstance(other, Lion):
            return Lion()



