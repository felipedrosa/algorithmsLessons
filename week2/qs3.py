import sys

def partition(alist, first, last):
  global count
  count = count + last - first
  pivot = alist[first]
  i = first + 1
  j = i
  while j <= last:
    if alist[j] < pivot:
      aux = alist[i]
      alist[i] = alist[j]
      alist[j] = aux
      i += 1
    j += 1
  aux = alist[first]
  alist[first] = alist[i-1]
  alist[i-1] = aux
    
  return i-1
  
def quicksort(alist, first, last):
  if first < last:	
    if (last-first)%2==0: #if list has odd number of elements 0 1 2
      middle = first + (last-first)/2
    else: #if the array has even number of elements 0 1 2 3
      middle = first + (last-first-1)/2
    
    a = alist[first]
    b = alist[middle]
    c = alist[last]
    median = (a + b + c) - min(a, b, c) - max(a, b, c)
    
    if median == alist[middle]:
      aux = alist[middle]
      alist[middle]=alist[first]
      alist[first]= aux
    elif median == alist[last]:
      aux = alist[last]
      alist[last] = alist[first]
      alist[first] = aux
    
    p = partition(alist, first, last)
    quicksort(alist, first, p-1) 
    quicksort(alist, p+1, last)

count = 0

print sys.argv[0]
#f = open('inputs.txt', 'r')
f = open(sys.argv[1], 'r')
alist = []

for line in f:
  alist.append(int(line))

quicksort(alist,0,len(alist)-1)
print count