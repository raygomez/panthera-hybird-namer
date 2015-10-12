from __future__ import print_function
from Jaguar import Jaguar
from Leopard import Leopard
from Liger import Liger
from Liguar import Liguar
from Lipard import Lipard
from Panthera import Panthera
from Tiger import Tiger

__author__ = 'raygomez'

class Lion(Panthera):

    def getMaleName(self):
        return 'Lion'

    def getFemaleName(self):
        return 'Lioness'

    def getOffspring(self, other):
        if isinstance(other, Lion):
            return Lion()
        elif isinstance(other, Tiger):
            return Liger()
        elif isinstance(other, Jaguar):
            return Liguar()
        elif isinstance(other, Leopard):
            return Lipard()
        Panthera.getOffspring(self, other)


