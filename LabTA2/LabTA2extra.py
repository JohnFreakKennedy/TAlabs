def insertion_sort(arr):                        #insertion sort
    counter = 0
    for i in range(0, len(arr)):
        j = i - 1
        b = arr[i]
        while( j >= 0 and arr[j] > b):
            counter = counter + 1
            arr[j + 1] = arr[j]
            arr[j] = b
            j = j - 1
        counter = counter + 1
    return counter
arr1=[8, 3, 1, 5, 2, 7]
print(arr1)
counter=insertion_sort(arr1)
print(arr1)
print(counter)
