from __future__ import division
import numpy as np,scipy as sp
import math,pylab,time,matplotlib.pyplot as pyplt

#
#
#
#TODO:
#   check results?
#       Breaks if too high K
#   vectorize all the things
#   improve calculating square distances!!
#   sparse Rnk matrix replace by dict?
#   moving demo

def runKMeans(K,dataset):

  #load data file
  X = np.loadtxt(dataset)

  #get rows and col info!
  N,D = X.shape

  #choose random points to initialize!
  randInits = np.arange(N)
  np.random.shuffle(randInits)
  Kmus =  X[randInits[:K]] #K by D array!

  print Kmus
  maxiters=10
  pyplt.ion()
  for i in range(maxiters):

    sqDmat = calcSqDist(X,Kmus)

    Rnk = determineRnk(sqDmat)

    KmusOld = Kmus

    Kmus = recalcMus(X,Rnk)
    #time.sleep(1)
  plotCurrent(X,Rnk,Kmus)

def calcSqDist(X,Kmus):
  N = X.shape[0]
  K = Kmus.shape[0]
  d = np.zeros( (N,K) )

  for n in range(N):
    for k in range(K):
      d[n][k] = euclideanDist(X[n],Kmus[k]) ** 2

  return d

def euclideanDist(X,Y):
  return math.sqrt( sum( [(x - y) ** 2 for (x,y) in zip(X,Y)]) )

def determineRnk(sqDmat):
  N,K = sqDmat.shape
  sqDmat2 = np.zeros( (N,K) )

  for n in range(N):
    miny = min(sqDmat[n])
    for k in range(K):

      if miny == sqDmat[n][k]:
        sqDmat2[n][k] = 1
        break

  return sqDmat2

def recalcMus(X,Rnk):
  N,K = Rnk.shape
  D = X.shape[1]

  Kmus = np.zeros( (K,D) )
  for k in range(K):
    denom = 0
    for n in range(N):
      Kmus[k] += (Rnk[n][k] * X[n])
      denom += Rnk[n][k]
    Kmus /= denom

  print Kmus
  return Kmus

#limited to K <= 7
def plotCurrent(X,Rnk,Kmus):

  N,D = X.shape
  K = Kmus.shape[0]

  colorMapping = ['b','y','r','c','m','g','k']
  colorVect = [""]* N

#terrible!!! figure out better way for colors!!!
  for n in range(N):
    for k in range(K):
      if Rnk[n][k] == 1:
        colorVect[n] = colorMapping[k]


  xData,yData = np.hsplit(X,2)
  pyplt.clf()
  pyplt.scatter(xData,yData,c=colorVect)
  pyplt.show()
  #print colorVect
  #print Kmus

if  __name__ == "__main__":
    runKMeans(2,"scaledfaithful.txt")
