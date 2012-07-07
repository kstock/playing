from __future__ import division

#TODO
#replicate All stats pg31,33 plots w/ matplotlib

#returns a list of possible coin flip results for n flips!!
def coin_flip(n):
  flips = ['H','T']
  newFlip = ['H','T']

  for i in range(n-1):
    flips = [x + y for x in flips for y in newFlip]

  return flips


#random variable, counts number of heads
def numH(flip):
  return flip.count('H')

#cumulative distribution function
def cdf(dist,x):
  rand_var = map(numH,dist)
  return len(filter(lambda ex: ex <= x,rand_var) )/len(dist)
  
def pmf(dist,x):
  rand_var = map(numH,dist)
  return rand_var.count(x) / len(dist)
