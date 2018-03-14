#!/usr/bin/python3

import random as rng
import numpy as np
from copy import deepcopy
import pprint as ppt

### Constants ###
NB_CARDS = 6

### Functions ###
def first_top_bottom():
    """
    In this shuffle, we take the first card and
    with probability half we put it on top of the deck
    with probality half we put it on the bottom of the deck

    return : the shuffle matrix of size NB_CARDS
    """
    identity = NB_CARDS * np.identity(NB_CARDS)
    # First outcome, the deck isn't changed
    shuffled_deck_1 = deepcopy(identity)
    # Second outcome, the first card is at the bottom and every other cards goes
    # up
    shuffled_deck_2 = deepcopy(identity)
    for i in range(NB_CARDS-1):
        shuffled_deck_2[i] = deepcopy(identity[i+1])
    shuffled_deck_2[NB_CARDS-1] = deepcopy(identity[0])
    # Now we have to combine the two outcome with probability half
    return (shuffled_deck_1 + shuffled_deck_2)/2

def shuffle_n_times(matrix,n):
    """
    Compute the shuffle matrix multiplied n times
    """
    res = deepcopy(matrix)
    for k in range(n):
        res = np.dot(res,matrix)/NB_CARDS
    return res

### Main ###
NB_SHUFFLE = 200
print("first_top_bottom, ",NB_SHUFFLE," times, with ", NB_CARDS, " cards.")
print(shuffle_n_times(first_top_bottom(),NB_SHUFFLE))
