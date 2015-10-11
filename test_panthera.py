from __future__ import print_function
from unittest import TestCase
from Lion import Lion

__author__ = 'raygomez'


class TestPanthera(TestCase):

    def testRaiseExceptionIfSameGender(self):

        lion1 = Lion('M')
        lion2 = Lion('M')

        with self.assertRaises(TypeError):
            lion1 + lion2


