from __future__ import print_function
from Panthera import Panthera

__author__ = 'raygomez'

class Lion(Panthera):

    def __init__(self, gender):
        Panthera.__init__(self, 'Lion', gender)

    def getMaleName(self):
        return 'Li'

    def getFemaleName(self):
        return 'oness'
