#write a function that creates an array from the users input and also print the index of the value the users requests

from array import *

arr = array('i', [])

n = int(input('Enter the number of values you\'d love to enter '))

for i in range(n):
    x = int(input('Enter next value '))
    arr.append(x)

print(arr)

k = 0
search = int(input('which number do you want to search? '))
for e in arr:
    if search == arr[k]:
        print(k)
        break
    k += 1 
    if search not in arr:
        print('Number not in array')
        break

print(arr.index(search))
