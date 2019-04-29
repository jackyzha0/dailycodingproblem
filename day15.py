'''
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
'''

import random

def getfromstream(stream):
    element = stream[0]
    for i range(len(stream)):
        if random.randint(0,i) == 1:
            element = strea[i]

    return element
