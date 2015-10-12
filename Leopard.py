from __future__ import print_function
import Jaguar
from Leguar import Leguar
from Leoger import Leoger
from Leopon import Leopon
import Lion
from Panthera import Panthera
import Tiger

__author__ = 'raygomez'


class Leopard(Panthera):
    def getMaleName(self):
        return 'Leopard'

    def getFemaleName(self):
        return 'Leopardess'

    def getOffspring(self, other):
        if isinstance(other, Leopard):
            return Leopard()
        elif isinstance(other, Lion.Lion):
            return Leopon()
        elif isinstance(other, Tiger.Tiger):
            return Leoger()
        elif isinstance(other, Jaguar.Jaguar):
            return Leguar()
        Panthera.getOffspring(self, other)