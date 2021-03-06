from __future__ import print_function
import random
from unittest import TestCase
from Jagger import Jagger
from Jagjagupard import Jagjagupard
from Jagleguar import Jagleguar
from Jagliger import Jagliger
from Jagliguar import Jagliguar
from Jaglion import Jaglion
from Jagtigon import Jagtigon
from Jaguar import Jaguar
from Jagupard import Jagupard
from Leguar import Leguar
from Leoger import Leoger
from Leojagupard import Leojagupard
from Leoleguar import Leoleguar
from Leoliger import Leoliger
from Leoliguar import Leoliguar
from Leoligulor import Leoligulor
from Leopard import Leopard
from Leopon import Leopon
from Leotigon import Leotigon
from Liger import Liger
from Liguar import Liguar
from Lijagupard import Lijagupard
from Lileguar import Lileguar
from Liliger import Liliger
from Liliguar import Liliguar
from Lililiger import Lililiger
from Lion import Lion
from Lipard import Lipard
from Litigon import Litigon
from Tigard import Tigard
from Tiger import Tiger
from Tigon import Tigon
from Tiguar import Tiguar
from Tijagupard import Tijagupard
from Tileguar import Tileguar
from Tiliger import Tiliger
from Tiliguar import Tiliguar
from Titigon import Titigon

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
        self.assertIsInstance(offspring, Lion)
        self.assertEqual(1, offspring.generation)

    def testOffspringOfLionAndTigress(self):

        offspring = self.lion1 + self.tigress1

        if offspring.gender == 'M':
            self.assertEqual('Liger', offspring.name)
        else:
            self.assertEqual('Ligress', offspring.name)

        self.assertIsInstance(offspring, Liger)
        self.assertEqual(2, offspring.generation)

        offspring = self.tigress1 + self.lion1

        if offspring.gender == 'M':
            self.assertEqual('Liger', offspring.name)
        else:
            self.assertEqual('Ligress', offspring.name)
        self.assertIsInstance(offspring, Liger)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfLionAndJaguaress(self):

        offspring = self.lion1 + self.jaguaress1

        if offspring.gender == 'M':
            self.assertEqual('Liguar', offspring.name)
        else:
            self.assertEqual('Liguaress', offspring.name)
        self.assertIsInstance(offspring, Liguar)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfLionAndLeopardess(self):

        offspring = self.lion1 + self.leopardess1

        if offspring.gender == 'M':
            self.assertEqual('Lipard', offspring.name)
        else:
            self.assertEqual('Lipardess', offspring.name)
        self.assertIsInstance(offspring, Lipard)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfLionAndLigress(self):

        offspring = self.lion1 + self.ligress1

        if offspring.gender == 'M':
            self.assertEqual('Liliger', offspring.name)
        else:
            self.assertEqual('Liligress', offspring.name)
        self.assertIsInstance(offspring, Liliger)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLionAndTigoness(self):

        offspring = self.lion1 + self.tigoness1

        if offspring.gender == 'M':
            self.assertEqual('Litigon', offspring.name)
        else:
            self.assertEqual('Litigoness', offspring.name)
        self.assertIsInstance(offspring, Litigon)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLionAndJagupardess(self):

        offspring = self.lion1 + self.jagupardess1

        if offspring.gender == 'M':
            self.assertEqual('Lijagupard', offspring.name)
        else:
            self.assertEqual('Lijagupardess', offspring.name)
        self.assertIsInstance(offspring, Lijagupard)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLionAndLeguaress(self):

        offspring = self.lion1 + self.leguaress1

        if offspring.gender == 'M':
            self.assertEqual('Lileguar', offspring.name)
        else:
            self.assertEqual('Lileguaress', offspring.name)
        self.assertIsInstance(offspring, Lileguar)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLionAndLiguaress(self):

        offspring = self.lion1 + self.liguaress1

        if offspring.gender == 'M':
            self.assertEqual('Liliguar', offspring.name)
        else:
            self.assertEqual('Liliguaress', offspring.name)
        self.assertIsInstance(offspring, Liliguar)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfTigerAndLioness(self):

        offspring = self.tiger1 + self.lioness1

        if offspring.gender == 'M':
            self.assertEqual('Tigon', offspring.name)
        else:
            self.assertEqual('Tigoness', offspring.name)
        self.assertIsInstance(offspring, Tigon)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfTigerAndTigress(self):

        offspring = self.tiger1 + self.tigress1

        if offspring.gender == 'M':
            self.assertEqual('Tiger', offspring.name)
        else:
            self.assertEqual('Tigress', offspring.name)
        self.assertIsInstance(offspring, Tiger)
        self.assertEqual(1, offspring.generation)

    def testOffspringOfTigerAndJaguaress(self):

        offspring = self.tiger1 + self.jaguaress1

        if offspring.gender == 'M':
            self.assertEqual('Tiguar', offspring.name)
        else:
            self.assertEqual('Tiguaress', offspring.name)
        self.assertIsInstance(offspring, Tiguar)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfTigerAndLeopardess(self):

        offspring = self.tiger1 + self.leopardess1

        if offspring.gender == 'M':
            self.assertEqual('Tigard', offspring.name)
        else:
            self.assertEqual('Tigardess', offspring.name)
        self.assertIsInstance(offspring, Tigard)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfTigerAndLigress(self):

        offspring = self.tiger1 + self.ligress1

        if offspring.gender == 'M':
            self.assertEqual('Tiliger', offspring.name)
        else:
            self.assertEqual('Tiligress', offspring.name)
        self.assertIsInstance(offspring, Tiliger)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfTigerAndTigoness(self):

        offspring = self.tiger1 + self.tigoness1

        if offspring.gender == 'M':
            self.assertEqual('Titigon', offspring.name)
        else:
            self.assertEqual('Titigoness', offspring.name)
        self.assertIsInstance(offspring, Titigon)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfTigerAndJagupardess(self):

        offspring = self.tiger1 + self.jagupardess1

        if offspring.gender == 'M':
            self.assertEqual('Tijagupard', offspring.name)
        else:
            self.assertEqual('Tijagupardess', offspring.name)
        self.assertIsInstance(offspring, Tijagupard)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfTigerAndLeguaress(self):

        offspring = self.tiger1 + self.leguaress1

        if offspring.gender == 'M':
            self.assertEqual('Tileguar', offspring.name)
        else:
            self.assertEqual('Tileguaress', offspring.name)
        self.assertIsInstance(offspring, Tileguar)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfTigerAndLiguaress(self):

        offspring = self.tiger1 + self.liguaress1

        if offspring.gender == 'M':
            self.assertEqual('Tiliguar', offspring.name)
        else:
            self.assertEqual('Tiliguaress', offspring.name)
        self.assertIsInstance(offspring, Tiliguar)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfJaguarAndLioness(self):

        offspring = self.jaguar1 + self.lioness1

        if offspring.gender == 'M':
            self.assertEqual('Jaglion', offspring.name)
        else:
            self.assertEqual('Jaglioness', offspring.name)
        self.assertIsInstance(offspring, Jaglion)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfJaguarAndTigress(self):

        offspring = self.jaguar1 + self.tigress1

        if offspring.gender == 'M':
            self.assertEqual('Jagger', offspring.name)
        else:
            self.assertEqual('Jaggress', offspring.name)
        self.assertIsInstance(offspring, Jagger)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfJaguarAndJaguaress(self):

        offspring = self.jaguar1 + self.jaguaress1

        if offspring.gender == 'M':
            self.assertEqual('Jaguar', offspring.name)
        else:
            self.assertEqual('Jaguaress', offspring.name)
        self.assertIsInstance(offspring, Jaguar)
        self.assertEqual(1, offspring.generation)

    def testOffspringOfJaguarAndLeopardess(self):

        offspring = self.jaguar1 + self.leopardess1

        if offspring.gender == 'M':
            self.assertEqual('Jagupard', offspring.name)
        else:
            self.assertEqual('Jagupardess', offspring.name)
        self.assertIsInstance(offspring, Jagupard)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfJaguarAndLigress(self):

        offspring = self.jaguar1 + self.ligress1

        if offspring.gender == 'M':
            self.assertEqual('Jagliger', offspring.name)
        else:
            self.assertEqual('Jagligress', offspring.name)
        self.assertIsInstance(offspring, Jagliger)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfJaguarAndTigoness(self):

        offspring = self.jaguar1 + self.tigoness1

        if offspring.gender == 'M':
            self.assertEqual('Jagtigon', offspring.name)
        else:
            self.assertEqual('Jagtigoness', offspring.name)
        self.assertIsInstance(offspring, Jagtigon)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfJaguarAndJagupardess(self):

        offspring = self.jaguar1 + self.jagupardess1

        if offspring.gender == 'M':
            self.assertEqual('Jagjagupard', offspring.name)
        else:
            self.assertEqual('Jagjagupardess', offspring.name)
        self.assertIsInstance(offspring, Jagjagupard)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfJaguarAndLeguaress(self):

        offspring = self.jaguar1 + self.leguaress1

        if offspring.gender == 'M':
            self.assertEqual('Jagleguar', offspring.name)
        else:
            self.assertEqual('Jagleguaress', offspring.name)
        self.assertIsInstance(offspring, Jagleguar)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfJaguarAndLiguaress(self):

        offspring = self.jaguar1 + self.liguaress1

        if offspring.gender == 'M':
            self.assertEqual('Jagliguar', offspring.name)
        else:
            self.assertEqual('Jagliguaress', offspring.name)
        self.assertIsInstance(offspring, Jagliguar)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLeopardAndLioness(self):

        offspring = self.leopard1 + self.lioness1

        if offspring.gender == 'M':
            self.assertEqual('Leopon', offspring.name)
        else:
            self.assertEqual('Leoponess', offspring.name)
        self.assertIsInstance(offspring, Leopon)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfLeopardAndTigress(self):

        offspring = self.leopard1 + self.tigress1

        if offspring.gender == 'M':
            self.assertEqual('Leoger', offspring.name)
        else:
            self.assertEqual('Leogress', offspring.name)
        self.assertIsInstance(offspring, Leoger)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfLeopardAndJaguaress(self):

        offspring = self.leopard1 + self.jaguaress1

        if offspring.gender == 'M':
            self.assertEqual('Leguar', offspring.name)
        else:
            self.assertEqual('Leguaress', offspring.name)
        self.assertIsInstance(offspring, Leguar)
        self.assertEqual(2, offspring.generation)

    def testOffspringOfLeopardAndLeopardess(self):

        offspring = self.leopard1 + self.leopardess1

        if offspring.gender == 'M':
            self.assertEqual('Leopard', offspring.name)
        else:
            self.assertEqual('Leopardess', offspring.name)
        self.assertIsInstance(offspring, Leopard)
        self.assertEqual(1, offspring.generation)

    def testOffspringOfLeopardAndLigress(self):

        offspring = self.leopard1 + self.ligress1

        if offspring.gender == 'M':
            self.assertEqual('Leoliger', offspring.name)
        else:
            self.assertEqual('Leoligress', offspring.name)
        self.assertIsInstance(offspring, Leoliger)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLeopardAndTigoness(self):

        offspring = self.leopard1 + self.tigoness1

        if offspring.gender == 'M':
            self.assertEqual('Leotigon', offspring.name)
        else:
            self.assertEqual('Leotigoness', offspring.name)
        self.assertIsInstance(offspring, Leotigon)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLeopardAndJagupardess(self):

        offspring = self.leopard1 + self.jagupardess1

        if offspring.gender == 'M':
            self.assertEqual('Leojagupard', offspring.name)
        else:
            self.assertEqual('Leojagupardess', offspring.name)
        self.assertIsInstance(offspring, Leojagupard)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLeopardAndLeguaress(self):

        offspring = self.leopard1 + self.leguaress1

        if offspring.gender == 'M':
            self.assertEqual('Leoleguar', offspring.name)
        else:
            self.assertEqual('Leoleguaress', offspring.name)
        self.assertIsInstance(offspring, Leoleguar)
        self.assertEqual(3, offspring.generation)

    def testOffspringOfLeopardAndLiguaress(self):

        offspring = self.leopard1 + self.liguaress1

        if offspring.gender == 'M':
            self.assertEqual('Leoliguar', offspring.name)
        else:
            self.assertEqual('Leoliguaress', offspring.name)
        self.assertIsInstance(offspring, Leoliguar)
        self.assertEqual(3, offspring.generation)

    def testOffspringLeoponAndLiguaress(self):

        leopon1 = Leopon('M')
        liguaress1 = Liguar('F')

        offspring = leopon1 + liguaress1
        self.assertEqual('Leoligulor', offspring.name)
        self.assertIsInstance(offspring, Leoligulor)
        self.assertEqual(3, offspring.generation)

    def testOffspringLionAndLiligress(self):
        liligress1 = Liliger('F')

        offspring = self.lion1 + liligress1

        if offspring.gender == 'M':
            self.assertEqual('Li-liliger', offspring.name)
        else:
            self.assertEqual('Li-liligress', offspring.name)
        self.assertIsInstance(offspring, Lililiger)
        self.assertEqual(4, offspring.generation)

    def testSortingSameGeneration(self):
        lion = Lion()
        tiger = Tiger()
        jaguar = Jaguar()
        leopard = Leopard()
        list_of_animals = [lion, tiger, jaguar, leopard]
        list_of_animals.sort()

        self.assertEqual(jaguar, list_of_animals[0])
        self.assertEqual(leopard, list_of_animals[1])
        self.assertEqual(lion, list_of_animals[2])
        self.assertEqual(tiger, list_of_animals[3])

    def testSortingDifferentGeneration(self):

        lion = Lion()
        tigon = Tigon()
        liligress = Liliger()
        lililiger = Lililiger()
        list_of_animals = [lililiger, lion, liligress, tigon]
        list_of_animals.sort()

        self.assertEqual(lion, list_of_animals[0])
        self.assertEqual(tigon, list_of_animals[1])
        self.assertEqual(liligress, list_of_animals[2])
        self.assertEqual(lililiger, list_of_animals[3])

    def testSortingDifferentGenerationWithShuffledList(self):

        lion = Lion()
        jaguar = Jaguar()
        tigon = Tigon()
        leguar = Leguar()
        liligress = Liliger()
        tiliguar = Tiliguar()
        lililiger = Lililiger()

        list_of_animals = [lililiger, tiliguar, lion, liligress, tigon, jaguar, leguar]

        random.shuffle(list_of_animals)
        list_of_animals.sort()

        self.assertEqual(jaguar, list_of_animals[0])
        self.assertEqual(lion, list_of_animals[1])
        self.assertEqual(leguar, list_of_animals[2])
        self.assertEqual(tigon, list_of_animals[3])
        self.assertEqual(liligress, list_of_animals[4])
        self.assertEqual(tiliguar, list_of_animals[5])
        self.assertEqual(lililiger, list_of_animals[6])
