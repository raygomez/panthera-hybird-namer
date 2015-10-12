from __future__ import print_function
from Panthera import Panthera

__author__ = 'ragomez'

class JagLion(Panthera):

    def __init__(self):
        Panthera.__init__(self)
        self.generation = 2

    def getMaleName(self):
        return 'JagLion'

    def getFemaleName(self):
        return 'JagLioness'

    def getOffspring(self, other):
        if isinstance(other, JagLion):
            return JagLion()

        Panthera.getOffspring(self,other)

