from __future__ import print_function
import random
from Panthera import Panthera

__author__ = 'ragomez'

class Jagger(Panthera):

    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 2

    def getMaleName(self):
        return 'Jagger'

    def getFemaleName(self):
        return 'Jaggress'

    def getOffspring(self, other):
        if isinstance(other, Jagger):
            return Jagger()

        Panthera.getOffspring(self,other)

