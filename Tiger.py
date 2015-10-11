from __future__ import print_function
from Panthera import Panthera

__author__ = 'raygomez'


class Tiger(Panthera):

    def getMaleName(self):
        return 'Tiger'

    def getFemaleName(self):
        return 'Tigress'

    def getOffspring(self, other):
        if isinstance(other, Tiger):
            return Tiger()

