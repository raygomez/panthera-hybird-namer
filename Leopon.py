from __future__ import print_function
import random

from Leoligulor import Leoligulor
import Liguar
from Panthera import Panthera

__author__ = 'ragomez'


class Leopon(Panthera):

    def __init__(self, gender = random.choice('MF')):
        Panthera.__init__(self, gender)
        self.generation = 2

    def getMaleName(self):
        return 'Leopon'

    def getFemaleName(self):
        return 'Leoponess'

    def getOffspring(self, other):

        if isinstance(other, Liguar.Liguar):
            return Leoligulor()
        elif isinstance(other, Leopon):
            return Leopon()

        Panthera.getOffspring(self,other)

