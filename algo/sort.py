#Sorting and Searching Algorithms!


#bubble sort
#worst: O(n^2) best: O(n)
def bub(a):
  for each in a:
    for i in range(0,len(a) - 1):
      if a[i] > a[i+1]:
        a[i], a[i+1] = a[i+1],a[i]

#odd even sort
def oddEven(a):
  sort = False
  while(not sort):
    sort = True
    for i in range(1,len(a) -1, 2):
      if a[i] > a[i+1]:
        a[i],a[i+1] = a[i+1],a[i]
        sort = False    
    for i in range(0,len(a) -1, 2):
      if a[i] > a[i+1]:
        a[i],a[i+1] = a[i+1],a[i]
        sort = False   

#gnome sort
def gnome(a):
  pos = 1
  while pos < len(a):
    if a[pos] >= a[pos-1]:
      pos += 1
    else:
      a[pos],a[pos-1] = a[pos-1],a[pos]
      if pos > 1:
        pos += -1
      else:
        pos += 1


#insertion sort
def inser(a):
  for j in range(1, len(a)):
    key = a[j]
    i = j - 1
    while i >= 0 and a[i] > key:
      a[i], a[j] = a[j], a[i]
      j = i
      i += -1 


#merge sort
#merge: call to sort list
#mergeCat: does the compare+concats
def merge(a):
  if len(a) <= 1:
    return a
  mid = len(a)/2 
  left = a[:mid]
  right = a[mid:]
  left = merge(left)
  right = merge(right)
  result = mergeCat(left,right)
  return result

def mergeCat(left,right):
  result = []
  while len(left) > 0 or len(right) > 0:
    if len(left) > 0 and len(right) > 0:
      if left[0] <= right[0]:
        result.append(left[0])
        left = left[1:]
      else:
        result.append(right[0])
        right = right[1:]
    elif len(left) > 0:
      result.append(left[0])
      left = left[1:]
    elif len(right) > 0:
      result.append(right[0])
      right = right[1:]
  return result


#selection sort
def sel(a):
  for i in range(0,len(a) - 1):
    #get index of minimum value of rest of list
    temp =  a.index(min(a[i:]))
    #swap vals
    a[temp], a[i] = a[i], a[temp]

#counting sort
#can only sort positive integers
#pretty shitty non-comparative sort
def countS(a):
  count = [0 for x in range(0,max(a) + 1)]
  total = 0
  result = []
  for i in range(0,len(a)):
    count[a[i]] += 1
    total += 1
  for i in range(0,total):
    while count[i] > 0:
      result.append(i)
      count[i] -= 1
  return result


#quicksort  
#O(n log n) comparisons
def quick(a):
  if len(a) <= 1:
    return a
  pivot = len(a)/2
  less = []
  more = []
  piv = a[pivot]
  del a[pivot]
  for x in a:
    if x<= piv:
      less.append(x)
    else:
      more.append(x)
  return quick(less) + [piv] + quick(more) 

#uses quicksort on long lists, but
#uses insertion sort when list becomes size 6
def hyQI(a):
  if len(a) <= 6:
    return inser(a)
  pivot = len(a)/2
  less = []
  more = []
  piv = a[pivot]
  del a[pivot]
  for x in a:
    if x<= piv:
      less.append(x)
    else:
      more.append(x)
  return quick(less) + [piv] + quick(more) 



#shell sort
def shell(a):
  inc = len(a)/2 
  while inc > 0:
    for j in range(inc,len(a)):
      temp = a[j]
      while j >= inc and a[j-inc] > temp:
        a[j] = a[j-inc]
        j = j - inc
      a[j] = temp
    inc = int(inc/2.2)

def wtf(x = 5):
  if 2 < x < 10:
    print x, "is between 2 and 10"
  if x in [1,2,3,8]:
    print x, "is in [1,2,3,8]"

#binary search
def binSearch(a,value, low = 0, high = None):
  if high == None:
    high = len(a) - 1
  if high < low:
		return -1
  mid = low + (high - low)/2
  if a[mid] > value:
    return binSe(a,value,low, mid - 1)
  elif a[mid] < value:
    return binSe(a, value, mid+1,high)
  else:
    return mid

#terrible exhaustive search
def nSearch(a,val):
  found = -1
  for i in a:
    if i == val:
      return a.index(i)
  return found


#compares sorting times
from time import time
import sys
def testSorts():
  sys.setrecursionlimit(20000)
  n = 2
  t1 = 0
  t2 = 0
  timeB = []
  timeQ = []
  timeQI = []
  a = [3,2,1]
  while n < 3000:
    b = a * n
    t1 = time()
    bub(b)
    t2 = time()
    timeB.append(t2 - t1)
    b = a * n
    t1 = time()
    hyQI(b)
    t2 = time()
    timeQI.append(t2 - t1)
    b = a * n
    t1 = time()
    quick(b)
    t2 = time()
    timeQ.append(t2 - t1)
    n += 1000
  print "it takes bubble sort : ", timeB
  print "it takes quicksort: ", timeQ
  print "it takes hydrid quick/insertion: ", timeQI






