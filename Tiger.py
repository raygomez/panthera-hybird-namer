from __future__ import print_function
import Jaguar
import Leopard
import Lion
from Panthera import Panthera
from Tigard import Tigard
import Tigon
import Tiguar

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
        Panthera.getOffspring(self, other)
