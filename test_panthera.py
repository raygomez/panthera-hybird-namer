from __future__ import print_function
from unittest import TestCase
from Jaguar import Jaguar
from Leopard import Leopard
from Lion import Lion
from Tiger import Tiger

__author__ = 'raygomez'


class TestPanthera(TestCase):

    def testRaiseExceptionIfSameGender(self):

        lion1 = Lion('M')
        lion2 = Lion('M')

        with self.assertRaises(TypeError):
            lion1 + lion2

    def testOffspringOfLionAndLioness(self):

        lion1 = Lion('M')
        lioness2 = Lion('F')

        offspring = lion1 + lioness2

        if offspring.gender == 'M':
            self.assertEqual('Lion', offspring.name)
        else:
            self.assertEqual('Lioness', offspring.name)
        self.assertEqual(1, offspring.generation)

    def testOffspringOfLionAndTigress(self):

        lion1 = Lion('M')
        tigress2 = Tiger('F')

        offspring = lion1 + tigress2

        if offspring.gender == 'M':
            self.assertEqual('Liger', offspring.name)
        else:
            self.assertEqual('Ligress', offspring.name)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfTigerAndTigress(self):

        tiger = Tiger('M')
        tigress = Tiger('F')

        offspring = tiger + tigress

        if offspring.gender == 'M':
            self.assertEqual('Tiger', offspring.name)
        else:
            self.assertEqual('Tigress', offspring.name)
        self.assertEqual(1, offspring.generation)

    def testOffspringOfJaguarAndJaguaress(self):

        jaguar = Jaguar('M')
        jaguaress = Jaguar('F')

        offspring = jaguar + jaguaress

        if offspring.gender == 'M':
            self.assertEqual('Jaguar', offspring.name)
        else:
            self.assertEqual('Jaguaress', offspring.name)
        self.assertEqual(1, offspring.generation)

    def testOffspringOfLeopardAndLeopard(self):

        leopard = Leopard('M')
        leopardess = Leopard('F')

        offspring = leopard + leopardess

        if offspring.gender == 'M':
            self.assertEqual('Leopard', offspring.name)
        else:
            self.assertEqual('Leopardess', offspring.name)
        self.assertEqual(1, offspring.generation)
