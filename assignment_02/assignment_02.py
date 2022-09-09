
# defining a function sample that inputs 10 integers from the user to create the sample set
def sampleset(n):
  lst = []
  for i in range(n):
    try:
      x = int(input("Enter the {}th integer:".format(i)))
      lst.append(x)
    except:
      print('A non-integer value entered. Please enter an integer.')
  print("The entered numbers are:", lst)
  return lst

# functions to generate descriptive statistics
def minimum(lst):
  minval = lst[0]
  for i in lst:
    if i < minval:
      minval = i
  return minval

def maximum(lst):
  maxval = lst[0]
  for i in lst:
    if i > maxval:
      maxval = i
  return maxval

def range_(lst):
  minval =  minimum(lst)
  maxval =  maximum(lst)
  return (maxval - minval)

def mean_(lst):
  tot = 0
  for i in lst:
    tot += i
  return tot/len(lst)

def variance(lst):
  tot = 0
  avg = mean_(lst)
  for i in lst:
    tot += (i - avg)**2
  return tot/(len(lst)-1)

import math
def stdd(lst):
  var = variance(lst)
  return math.sqrt(var)

# calling the defined function
sample = sampleset(10)
print(minimum(sample))
print(maximum(sample))
print(range_(sample))
print(mean_(sample))
print(variance(sample))
print(stdd(sample))