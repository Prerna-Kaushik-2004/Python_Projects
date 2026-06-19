#Searchimg an element in a sequential order
from array import *
arr=array("i",[])
n=int(input("Enter the number of elements: "))
for i in range(n):
    arr.append(int(input("Enter the element: ")))
print("Original array: ",arr)

#searching 
flag=False
a=int(input("Enter the element to be searched: "))
for i in range(n-1):
    if (a==arr[i]):
        print(f"{a} is found at position {i+1}")
        flag=True
if flag==False:
    print("Not found in the array")
      