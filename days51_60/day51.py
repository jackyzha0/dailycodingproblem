'''
Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
'''
import random

def rand(k):
    return random.randint(0, k)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

def shuffle(deck):

    for i in range(0, len(deck)):
        j = rand(i)
        deck = swap(deck, i, j)
    
    return deck

deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 
       9, 10, 11, 12, 13, 14, 15, 
       16, 17, 18, 19, 20, 21, 22,  
       23, 24, 25, 26, 27, 28, 29, 
       30, 31, 32, 33, 34, 35, 36, 
       37, 38, 39, 40, 41, 42, 43,  
       44, 45, 46, 47, 48, 49, 50, 
       51]

print(shuffle(deck))
