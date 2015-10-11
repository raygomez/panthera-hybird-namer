from __future__ import print_function
import random

__author__ = 'raygomez'


class Panthera(object):
    def __init__(self, gender = random.choice('MF')):
        self.generation = 1

        if gender == 'M' or gender == 'F':
            self.gender = gender
            if gender == 'M':
                self.name = self.getMaleName()
            else:
                self.name = self.getFemaleName()
        else:
            raise TypeError('Invalid gender:{}'.format(gender))



    def __repr__(self):
        return '{}({},{})'.format(self.name, self.gender, self.generation)

    def __add__(self, other):
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

        return self.getOffspring(other)

    def getOffspring(self, other):
        raise NotImplementedError('GetOffspring should be implemented.')

    def getMaleName(self):
        raise NotImplementedError('GetMaleName should be implemented.')

    def getFemaleName(self):
        raise NotImplementedError('GetFemaleName should be implemented.')
