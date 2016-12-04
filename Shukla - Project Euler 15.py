# -*- coding: utf-8 -*-

'''Problem 15: Starting in the top left corner of a 2×2 grid, and
   only being able to move to the right and down, there are
   exactly 6 routes to the bottom right corner. How many such
   routes are there through a 20×20 grid?'''

'''For two points on a lattice seperated by an n-by-m rectangular
   sublattice, there are n+m choose n (or, equivalently, n+m
   choose m) Manhattan (L1 norm) paths between them.'''

import math

print math.factorial(40)/(math.factorial(20)*math.factorial(20))