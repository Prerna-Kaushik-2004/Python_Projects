#sorting array into ascending order
from array import *

arr_to_sort=array("i",[])
n=int(input("Enter the number of elements:"))
for i in range(n):
    arr_to_sort.append(int(input("Enter the element:")))
print("original array: ",arr_to_sort)

#bubble sort
flag=False
for i in range(n-1):
    for j in range(n-1-i):
        if (arr_to_sort[j]>arr_to_sort[j+1]):
            t=arr_to_sort[j]
            arr_to_sort[j]=arr_to_sort[j+1]
            arr_to_sort[j+1]=t
            flag=True
    if flag==False:
        break
    else:
        flag=False
print("Sorted array: ",arr_to_sort)        