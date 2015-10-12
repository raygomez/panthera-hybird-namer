from __future__ import print_function
from JagLion import JagLion
from Jagger import Jagger
from Jagupard import Jagupard
import Leopard
import Lion
from Panthera import Panthera
import Tiger

__author__ = 'raygomez'

class Jaguar(Panthera):

    def getMaleName(self):
        return 'Jaguar'

    def getFemaleName(self):
        return 'Jaguaress'

    def getOffspring(self, other):
        if isinstance(other, Lion.Lion):
            return JagLion()
        elif isinstance(other, Tiger.Tiger):
            return Jagger()
        elif isinstance(other, Leopard.Leopard):
            return Jagupard()
        if isinstance(other, Jaguar):
            return Jaguar()
        Panthera.getOffspring(self, other)
