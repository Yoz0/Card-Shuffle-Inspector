# Card Shuffle Inspector
A program designed to check if a shuffle is efficient -- by Stéphane Kastenbaum

## Introduction
Since a discussion I had with my friend I wanted to know if there is a way to 
compute how efficient is a shuffle. I don't want to do to much of statistics 
so I'm gonna bruteforce a little bit.

The goal is to program to compare different shuffling method. Idealy, in the end
I could implement every kind of shuffling method. 

## Representing a shuffle
A shuffle is a permutation. If I take the first card and put it to the end of my
deck, this is a simple cycle permutation. Yet when one shuffle a deck it usualy
involves randmness ("Take the first card and put it whether at the top or at
the bottom of the deck") So I need something better.

My idea is to use matrices (because matrices are cool) where Mij is the 
probability to put the *j* card at the *i* place. So I (the identity matrix) 
represent no shuffling, and for a deck of three card the matrix
[ 0 0 1
  0 1 0
  1 0 0 ]
represent the inversion of the first and the third card. 

Also we can represent the chance of card being at a place or at another. For 
example the matrix 
[ 1/3 1/3 1/3
  1/3 1/3 1/3
  1/3 1/3 1/3 ]
would be the perfect shuffling where every card have equal probability to be at 
every position.

It is important to notice that since two cards cannot be at the same place and
a card cannot be at two different place, the sum of the probabilites over a line
and over a column equal to 1.

With this method we do not differenciate a shuffle method and the state of 
a deck of cards, this is covenient since the state is "the shuffle applied to 
the identity matrix"

## Computing the shuffle matrix
In the real world people often choose a shuffle method and apply it multiple 
time on the same deck. It can be represented on my method by finding the matrix
of a single shuffle, and multiple the matrix by itself.

### Finding the single shuffle matrix
For some kind of shuffle method the matrix can be found by hand, but I think
this could be hard and boring to find the right matrix for some shuffling 
moethod, the [faro shuffle](https://en.wikipedia.org/wiki/Faro_shuffle) for 
example.

So what I'm gonna do, is creating a function which will do the said shuffle on a
list and then call it many times and finding the mean of the shuffled states.

##Implementation
To do this I will use :
* Python 3
* Numpy to represent the matrices
* random to generate randomness

### Note on the represntation of the matrices
Since every value of the matrices is inferior to 1 and approximation on small
number are quite bad in python I decided that I will miltiply the matricies by
the size of the deck. So with n the size of the deck n * I will be the deck
where each card is at its initial position and the matrix with 1 everywhere
will be the uniformely distributed one.

