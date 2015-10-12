from __future__ import print_function
from unittest import TestCase
from Jaguar import Jaguar
from Leopard import Leopard
from Lion import Lion
from Tiger import Tiger

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
        self.assertEqual(1, offspring.generation)

    def testOffspringOfTigerAndLeopardess(self):

        offspring = self.tiger1 + self.leopardess1

        if offspring.gender == 'M':
            self.assertEqual('Tigard', offspring.name)
        else:
            self.assertEqual('Tigardess', offspring.name)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfJaguarAndJaguaress(self):

        offspring = self.jaguar1 + self.jaguaress1

        if offspring.gender == 'M':
            self.assertEqual('Jaguar', offspring.name)
        else:
            self.assertEqual('Jaguaress', offspring.name)
        self.assertEqual(1, offspring.generation)

    def testOffspringOfLeopardAndLeopard(self):

        offspring = self.leopard1 + self.leopardess1

        if offspring.gender == 'M':
            self.assertEqual('Leopard', offspring.name)
        else:
            self.assertEqual('Leopardess', offspring.name)
        self.assertEqual(1, offspring.generation)
