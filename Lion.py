from __future__ import print_function
import Jaguar
import Leopard
import Liger
import Liguar
import Lipard
from Panthera import Panthera
import Tiger

__author__ = 'raygomez'


class Lion(Panthera):

    def getMaleName(self):
        return 'Lion'

    def getFemaleName(self):
        return 'Lioness'

    def getOffspring(self, other):
        if isinstance(other, Lion):
            return Lion()
        elif isinstance(other, Tiger.Tiger):
            return Liger.Liger()
        elif isinstance(other, Jaguar.Jaguar):
            return Liguar.Liguar()
        elif isinstance(other, Leopard.Leopard):
            return Lipard.Lipard()
        Panthera.getOffspring(self, other)


