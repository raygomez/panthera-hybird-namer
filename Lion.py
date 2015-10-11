from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'raygomez'


class Lion(Panthera):

    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)

    def getMaleName(self):
        return 'Lion'

    def getFemaleName(self):
        return 'Lioness'

    def getOffspring(self, other):

        if isinstance(other, Lion):
            return Lion()



