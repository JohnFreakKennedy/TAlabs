import math
from random import randint
n = int(input("Введіть розмір масиву:"))
arr = []
arr2 = []
arr3 = []
for i in range(n):
    arr.append(randint(0, 100))
    arr2.append(arr[i])
    arr3.append(arr[i])
print(arr)
for i in range(n):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Відсортований масив(бульбашка):"+str(arr))
for i in range(n):
    for j in range(n-1):
        if arr2[j] % 2 == 1 and arr2[j+1] % 2 == 0:
            arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
        if arr2[j] % 2 == 1 and arr2[j + 1] % 2 == 1:
            if arr2[j] < arr2[j+1]:
                arr2[j], arr2[j+1] = arr2[j+1], arr3[j]
        if arr2[j] % 2 == 0 and arr2[j + 1] % 2 == 0:
            if arr2[j] > arr2[j + 1]:
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
print("Відсортований масив(2 завдання)"+str(arr2))
for i in range(n):
    for j in range(n - i - 1):
        if arr3[j] > arr3[j + 1]:
            arr3[j], arr3[j+1] = arr3[j+1], arr3[j]
        if arr3[j] > arr3[j + 1]:
            arr3[j], arr3[j+1] = arr3[j+1], arr3[j]
print("Відсортований масив(покращена бульбашка): "+str(arr3))

