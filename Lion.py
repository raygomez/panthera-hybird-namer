from __future__ import print_function
import Jaguar
import Jagupard
import Leguar
import Leopard
import Liger
import Liguar
from Lijagupard import Lijagupard
from Lileguar import Lileguar
from Liliger import Liliger
from Liliguar import Liliguar
import Lipard
from Litigon import Litigon
from Panthera import Panthera
import Tiger
import Tigon

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
        elif isinstance(other, Liger.Liger):
            return Liliger()
        elif isinstance(other, Tigon.Tigon):
            return Litigon()
        elif isinstance(other, Jagupard.Jagupard):
            return Lijagupard()
        elif isinstance(other, Leguar.Leguar):
            return Lileguar()
        elif isinstance(other, Liguar.Liguar):
            return Liliguar()
        Panthera.getOffspring(self, other)


