from __future__ import print_function
import Jaguar
import Jagupard
import Leguar
import Leoger
import Leojagupard
import Leoleguar
import Leoliger
import Leoliguar
import Leopon
import Leotigon
import Liger
import Liguar
import Lion
from Panthera import Panthera
import Tiger
import Tigon

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
            return Leopon.Leopon()
        elif isinstance(other, Tiger.Tiger):
            return Leoger.Leoger()
        elif isinstance(other, Jaguar.Jaguar):
            return Leguar.Leguar()
        elif isinstance(other, Liger.Liger):
            return Leoliger.Leoliger()
        elif isinstance(other, Tigon.Tigon):
            return Leotigon.Leotigon()
        elif isinstance(other, Jagupard.Jagupard):
            return Leojagupard.Leojagupard()
        elif isinstance(other, Leguar.Leguar):
            return Leoleguar.Leoleguar()
        elif isinstance(other, Liguar.Liguar):
            return Leoliguar.Leoliguar()
        Panthera.getOffspring(self, other)