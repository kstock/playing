# takes in polynomial of form c1 (x^n) + c2 (x^(n-1) + ... cn(x^0)
#                     represented as list of coefficients:
#                     x^4 - 3x^3 + 2 := [1, -3, 0, 0, 2]
#   finds local min!!

#code a generalization of 
#http://en.wikipedia.org/wiki/Gradient_descent#A_computational_example

#very susceptible to errors : /
#sometimes returns nan because of overflow in multiply:

#/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/numpy/lib/polynomial.py:642: RuntimeWarning: invalid value encountered in multiply
#  y = x * y + p[i]

#decreasing step size seems to fix this!!

import numpy as np

def sse(t,y):
  if len(t) != len(y):
    print "ERROR!!! Not same size in sse!"
  return .5 * (sum( [(t_i - y_i)**2 for (t_i,y_i) in zip(t,y)] ))

class gradDescent: 

  def __init__(self,funct,x_old = 0,x_new = 6,
               eps = .001,precision = .00001):
    
    self.funct = np.poly1d(funct)
    self.der1 = self.funct.deriv(m=1) #first derivative!!
    
    x_old = x_old
    x_new = x_new 
    eps = eps# step size
    precision = precision
    
    while abs(x_new - x_old) > precision:
       # print x_old
        x_old = x_new
        x_new = x_old - eps * self.f_prime(x_old)
    print "Local minimum occurs at ", x_new


    
  def f_prime(self,x):
      return self.der1(x)

if __name__ == "__main__":
#test!
  gradDescent( [1,-3,0,0,2] )
  gradDescent( [2,-3,0,0,2] )
  gradDescent( [2,-4,0,0,2] )
