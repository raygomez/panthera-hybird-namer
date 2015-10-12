from __future__ import print_function
import Jaguar
import Jagupard
import Leguar
import Leopard
import Liger
import Liguar
import Lion
from Panthera import Panthera
from Tigard import Tigard
import Tigon
import Tiguar
from Tijagupard import Tijagupard
from Tileguar import Tileguar
from Tiliger import Tiliger
from Tiliguar import Tiliguar
from Titigon import Titigon

__author__ = 'raygomez'


class Tiger(Panthera):

    def getMaleName(self):
        return 'Tiger'

    def getFemaleName(self):
        return 'Tigress'

    def getOffspring(self, other):
        if isinstance(other, Tiger):
            return Tiger()
        elif isinstance(other, Lion.Lion):
            return Tigon.Tigon()
        elif isinstance(other, Jaguar.Jaguar):
            return Tiguar.Tiguar()
        elif isinstance(other,  Leopard.Leopard):
            return Tigard()
        elif isinstance(other, Liger.Liger):
            return Tiliger()
        elif isinstance(other, Tigon.Tigon):
            return Titigon()
        elif isinstance(other, Jagupard.Jagupard):
            return Tijagupard()
        elif isinstance(other, Leguar.Leguar):
            return Tileguar()
        elif isinstance(other, Liguar.Liguar):
            return Tiliguar()
        Panthera.getOffspring(self, other)
