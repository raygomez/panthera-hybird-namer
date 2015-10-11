from __future__ import print_function
import random

__author__ = 'raygomez'


class Panthera(object):
    def __init__(self, name, gender):
        self.name = name
        self.generation = 1
        self.gender = gender

    def __repr__(self):
        return '{}({},{})'.format(self.name, self.gender, self.generation)

    def __add__(self, other):
        offspring = Panthera("", random.choice('MF'))

        mother = None
        father = None

        if self.gender == 'M':
            father = self
        elif other.gender == 'M':
            father = other

        if self.gender == 'F':
            mother = self
        elif other.gender == 'F':
            mother = other

        if not mother or not father:
            raise TypeError('They are not compatible: {}:{}, {}:{}'.
                            format(self.name,self.gender,
                                   other.name, self.gender))

        offspring.name = self.getMaleName() + self.getFemaleName()
        if self.name == other.name:
            self.generation = self.generation
        else:
            offspring.generation = str(int(max(self.generation, other.generation)) + 1)
        return offspring

    def getMaleName(self):
        raise NotImplementedError('Not implemented')

    def getFemaleName(self):
        raise NotImplementedError('Not implemented')