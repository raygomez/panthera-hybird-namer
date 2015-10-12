from __future__ import print_function
from Panthera import Panthera

__author__ = 'ragomez'

class Leopon(Panthera):

    def __init__(self):
        Panthera.__init__(self)
        self.generation = 2

    def getMaleName(self):
        return 'Leopon'

    def getFemaleName(self):
        return 'Leoponess'

    def getOffspring(self, other):
        if isinstance(other, Leopon):
            return Leopon()

        Panthera.getOffspring(self,other)

