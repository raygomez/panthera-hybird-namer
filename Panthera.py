from __future__ import print_function
import random

__author__ = 'raygomez'


class Panthera(object):
    def __init__(self, gender):
        self.name = ''
        self.generation = gender
        self.gender = ''

    def __add__(self, other):
        offspring = Panthera(random.choice('MF'))
        father = self if self.gender == 'M' else other
        mother = self if self.gender == 'F' else other

        if not mother or not father:
            raise TypeError('They are not compatible: {}:{}, {}:{}'.format(self.name,self.gender,
                                                                           other.name, self.gender))

        offspring.name = self.getMaleName() + self.getFemaleName()
        offspring.generation = max(self.generation, other.generation) + 1
        return offspring

    def getMaleName(self):
        raise NotImplementedError('Not implemented')

    def getFemaleName(self):
        raise NotImplementedError('Not implemented')