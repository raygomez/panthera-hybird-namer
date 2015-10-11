from __future__ import print_function
from unittest import TestCase
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

    def testOffspringOfTigerAndTrigress(self):

        tiger = Tiger('M')
        tigress = Tiger('F')

        offspring = tiger + tigress

        if offspring.gender == 'M':
            self.assertEqual('Tiger', offspring.name)
        else:
            self.assertEqual('Tigress', offspring.name)
        self.assertEqual(1, offspring.generation)
