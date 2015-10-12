from __future__ import print_function
import JagLion
import Jagger
import Jagjagupard
import Jagleguar
import Jagliger
import Jagliguar
import Jagtigon
import Jagupard
import Leguar
import Leopard
import Liger
import Liguar
import Lion
from Panthera import Panthera
import Tiger
import Tigon

__author__ = 'raygomez'


class Jaguar(Panthera):

    def getMaleName(self):
        return 'Jaguar'

    def getFemaleName(self):
        return 'Jaguaress'

    def getOffspring(self, other):
        if isinstance(other, Lion.Lion):
            return JagLion.JagLion()
        elif isinstance(other, Tiger.Tiger):
            return Jagger.Jagger()
        elif isinstance(other, Leopard.Leopard):
            return Jagupard.Jagupard()
        elif isinstance(other, Liger.Liger):
            return Jagliger.Jagliger()
        elif isinstance(other, Tigon.Tigon):
            return Jagtigon.Jagtigon()
        elif isinstance(other, Jagupard.Jagupard):
            return Jagjagupard.Jagjagupard()
        elif isinstance(other, Leguar.Leguar):
            return Jagleguar.Jagleguar()
        elif isinstance(other, Liguar.Liguar):
            return Jagliguar.Jagliguar()
        if isinstance(other, Jaguar):
            return Jaguar()
        Panthera.getOffspring(self, other)
