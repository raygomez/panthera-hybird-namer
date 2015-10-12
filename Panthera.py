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

        return father.getOffspring(mother)

    def getOffspring(self, other):
        raise NotImplementedError('Unknown hybrid: {} + {}'.format(self.__class__.__name__,
                                                                   other.__class__.__name__))
    def getMaleName(self):
        raise NotImplementedError('GetMaleName should be implemented.')

    def getFemaleName(self):
        raise NotImplementedError('GetFemaleName should be implemented.')

    def isMale(self):
        return self.gender == 'M'

    def isFemale(self):
        return self.gender == 'F'