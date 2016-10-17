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
    aux = alist[last]
    alist[last] = alist[first]
    alist[first] = aux
    p = partition(alist, first, last)
    quicksort(alist, first, p-1) 
    quicksort(alist, p+1, last)

count = 0
f = open('inputs.txt', 'r')
alist = []

for line in f:
  alist.append(int(line))

quicksort(alist,0,len(alist)-1)

print count