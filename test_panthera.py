from __future__ import print_function
from unittest import TestCase
from Jaguar import Jaguar
from Jagupard import Jagupard
from Leguar import Leguar
from Leopard import Leopard
from Liger import Liger
from Liguar import Liguar
from Lion import Lion
from Tiger import Tiger
from Tigon import Tigon

__author__ = 'raygomez'


class TestPanthera(TestCase):
    lion1 = Lion('M')
    lioness1 = Lion('F')
    tiger1 = Tiger('M')
    tigress1 = Tiger('F')
    jaguar1 = Jaguar('M')
    jaguaress1 = Jaguar('F')
    leopard1 = Leopard('M')
    leopardess1 = Leopard('F')
    ligress1 = Liger('F')
    tigoness1 = Tigon('F')
    jagupardess1 = Jagupard('F')
    leguaress1 = Leguar('F')
    liguaress1 = Liguar('F')

    def testRaiseExceptionIfSameGender(self):

        lion2 = Lion('M')

        with self.assertRaises(TypeError):
            self.lion1 + lion2

    def testOffspringOfLionAndLioness(self):

        offspring = self.lion1 + self.lioness1

        if offspring.gender == 'M':
            self.assertEqual('Lion', offspring.name)
        else:
            self.assertEqual('Lioness', offspring.name)
        self.assertEqual(1, offspring.generation)

    def testOffspringOfLionAndTigress(self):

        offspring = self.lion1 + self.tigress1

        if offspring.gender == 'M':
            self.assertEqual('Liger', offspring.name)
        else:
            self.assertEqual('Ligress', offspring.name)
        self.assertEqual(2, offspring.generation)

        offspring = self.tigress1 + self.lion1

        if offspring.gender == 'M':
            self.assertEqual('Liger', offspring.name)
        else:
            self.assertEqual('Ligress', offspring.name)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfLionAndJaguaress(self):

        offspring = self.lion1 + self.jaguaress1

        if offspring.gender == 'M':
            self.assertEqual('Liguar', offspring.name)
        else:
            self.assertEqual('Liguaress', offspring.name)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfLionAndLeopardess(self):

        offspring = self.lion1 + self.leopardess1

        if offspring.gender == 'M':
            self.assertEqual('Lipard', offspring.name)
        else:
            self.assertEqual('Lipardess', offspring.name)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfLionAndLigress(self):

        offspring = self.lion1 + self.ligress1

        if offspring.gender == 'M':
            self.assertEqual('Liliger', offspring.name)
        else:
            self.assertEqual('Liligress', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLionAndTigoness(self):

        offspring = self.lion1 + self.tigoness1

        if offspring.gender == 'M':
            self.assertEqual('Litigon', offspring.name)
        else:
            self.assertEqual('Litigoness', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLionAndJagupardess(self):

        offspring = self.lion1 + self.jagupardess1

        if offspring.gender == 'M':
            self.assertEqual('Lijagupard', offspring.name)
        else:
            self.assertEqual('Lijagupardess', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLionAndLeguaress(self):

        offspring = self.lion1 + self.leguaress1

        if offspring.gender == 'M':
            self.assertEqual('Lileguar', offspring.name)
        else:
            self.assertEqual('Lileguaress', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLionAndLiguaress(self):

        offspring = self.lion1 + self.liguaress1

        if offspring.gender == 'M':
            self.assertEqual('Liliguar', offspring.name)
        else:
            self.assertEqual('Liliguaress', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfTigerAndLioness(self):

        offspring = self.tiger1 + self.lioness1

        if offspring.gender == 'M':
            self.assertEqual('Tigon', offspring.name)
        else:
            self.assertEqual('Tigoness', offspring.name)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfTigerAndTigress(self):

        offspring = self.tiger1 + self.tigress1

        if offspring.gender == 'M':
            self.assertEqual('Tiger', offspring.name)
        else:
            self.assertEqual('Tigress', offspring.name)
        self.assertEqual(1, offspring.generation)

    def testOffspringOfTigerAndJaguaress(self):

        offspring = self.tiger1 + self.jaguaress1

        if offspring.gender == 'M':
            self.assertEqual('Tiguar', offspring.name)
        else:
            self.assertEqual('Tiguaress', offspring.name)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfTigerAndLeopardess(self):

        offspring = self.tiger1 + self.leopardess1

        if offspring.gender == 'M':
            self.assertEqual('Tigard', offspring.name)
        else:
            self.assertEqual('Tigardess', offspring.name)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfTigerAndLigress(self):

        offspring = self.tiger1 + self.ligress1

        if offspring.gender == 'M':
            self.assertEqual('Tiliger', offspring.name)
        else:
            self.assertEqual('Tiligress', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfTigerAndTigoness(self):

        offspring = self.tiger1 + self.tigoness1

        if offspring.gender == 'M':
            self.assertEqual('Titigon', offspring.name)
        else:
            self.assertEqual('Titigoness', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfTigerAndJagupardess(self):

        offspring = self.tiger1 + self.jagupardess1

        if offspring.gender == 'M':
            self.assertEqual('Tijagupard', offspring.name)
        else:
            self.assertEqual('Tijagupardess', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfTigerAndLeguaress(self):

        offspring = self.tiger1 + self.leguaress1

        if offspring.gender == 'M':
            self.assertEqual('Tileguar', offspring.name)
        else:
            self.assertEqual('Tileguaress', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfTigerAndLiguaress(self):

        offspring = self.tiger1 + self.liguaress1

        if offspring.gender == 'M':
            self.assertEqual('Tiliguar', offspring.name)
        else:
            self.assertEqual('Tiliguaress', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfJaguarAndLioness(self):

        offspring = self.jaguar1 + self.lioness1

        if offspring.gender == 'M':
            self.assertEqual('JagLion', offspring.name)
        else:
            self.assertEqual('JagLioness', offspring.name)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfJaguarAndTigress(self):

        offspring = self.jaguar1 + self.tigress1

        if offspring.gender == 'M':
            self.assertEqual('Jagger', offspring.name)
        else:
            self.assertEqual('Jaggress', offspring.name)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfJaguarAndJaguaress(self):

        offspring = self.jaguar1 + self.jaguaress1

        if offspring.gender == 'M':
            self.assertEqual('Jaguar', offspring.name)
        else:
            self.assertEqual('Jaguaress', offspring.name)
        self.assertEqual(1, offspring.generation)

    def testOffspringOfJaguarAndLeopardess(self):

        offspring = self.jaguar1 + self.leopardess1

        if offspring.gender == 'M':
            self.assertEqual('Jagupard', offspring.name)
        else:
            self.assertEqual('Jagupardess', offspring.name)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfJaguarAndLigress(self):

        offspring = self.jaguar1 + self.ligress1

        if offspring.gender == 'M':
            self.assertEqual('Jagliger', offspring.name)
        else:
            self.assertEqual('Jagligress', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfJaguarAndTigoness(self):

        offspring = self.jaguar1 + self.tigoness1

        if offspring.gender == 'M':
            self.assertEqual('Jagtigon', offspring.name)
        else:
            self.assertEqual('Jagtigoness', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfJaguarAndJagupardess(self):

        offspring = self.jaguar1 + self.jagupardess1

        if offspring.gender == 'M':
            self.assertEqual('Jagjagupard', offspring.name)
        else:
            self.assertEqual('Jagjagupardess', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfJaguarAndLeguaress(self):

        offspring = self.jaguar1 + self.leguaress1

        if offspring.gender == 'M':
            self.assertEqual('Jagleguar', offspring.name)
        else:
            self.assertEqual('Jagleguaress', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfJaguarAndLiguaress(self):

        offspring = self.jaguar1 + self.liguaress1

        if offspring.gender == 'M':
            self.assertEqual('Jagliguar', offspring.name)
        else:
            self.assertEqual('Jagliguaress', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLeopardAndLioness(self):

        offspring = self.leopard1 + self.lioness1

        if offspring.gender == 'M':
            self.assertEqual('Leopon', offspring.name)
        else:
            self.assertEqual('Leoponess', offspring.name)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfLeopardAndTigress(self):

        offspring = self.leopard1 + self.tigress1

        if offspring.gender == 'M':
            self.assertEqual('Leoger', offspring.name)
        else:
            self.assertEqual('Leogress', offspring.name)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfLeopardAndJaguaress(self):

        offspring = self.leopard1 + self.jaguaress1

        if offspring.gender == 'M':
            self.assertEqual('Leguar', offspring.name)
        else:
            self.assertEqual('Leguaress', offspring.name)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfLeopardAndLeopardess(self):

        offspring = self.leopard1 + self.leopardess1

        if offspring.gender == 'M':
            self.assertEqual('Leopard', offspring.name)
        else:
            self.assertEqual('Leopardess', offspring.name)
        self.assertEqual(1, offspring.generation)

    def testOffspringOfLeopardAndLigress(self):

        offspring = self.leopard1 + self.ligress1

        if offspring.gender == 'M':
            self.assertEqual('Leoliger', offspring.name)
        else:
            self.assertEqual('Leoligress', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLeopardAndTigoness(self):

        offspring = self.leopard1 + self.tigoness1

        if offspring.gender == 'M':
            self.assertEqual('Leotigon', offspring.name)
        else:
            self.assertEqual('Leotigoness', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLeopardAndJagupardess(self):

        offspring = self.leopard1 + self.jagupardess1

        if offspring.gender == 'M':
            self.assertEqual('Leojagupard', offspring.name)
        else:
            self.assertEqual('Leojagupardess', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLeopardAndLeguaress(self):

        offspring = self.leopard1 + self.leguaress1

        if offspring.gender == 'M':
            self.assertEqual('Leoleguar', offspring.name)
        else:
            self.assertEqual('Leoleguaress', offspring.name)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLeopardAndLiguaress(self):

        offspring = self.leopard1 + self.liguaress1

        if offspring.gender == 'M':
            self.assertEqual('Leoliguar', offspring.name)
        else:
            self.assertEqual('Leoliguaress', offspring.name)
        self.assertEqual(3, offspring.generation)

