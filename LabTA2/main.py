import numpy as np
import random
from lablib import plot_data

sizes = [10, 100, 1000, 10000]
types = ["random"]
data_plot = {'random': {'merge': {}, 'insertion': {}}}


def MergeSort(argShuffledList):
    intNumOfComp = 0
    if len(argShuffledList) > 1:
        intMidValue = len(argShuffledList)//2
        listLeftHalf = argShuffledList[:intMidValue]
        listRightHalf = argShuffledList[intMidValue:]
        left_part = MergeSort(listLeftHalf)
        right_part = MergeSort(listRightHalf)
        intNumOfComp += left_part[1] + right_part[1]
        i = 0
        j = 0
        k = 0
        while i < len(listLeftHalf) and j < len(listRightHalf):
            intNumOfComp += 1
            if listLeftHalf[i] < listRightHalf[j]:
                argShuffledList[k] = listLeftHalf[i]
                i = i+1
            else:
                argShuffledList[k] = listRightHalf[j]
                j = j+1
            k = k+1
        while i < len(listLeftHalf):
            argShuffledList[k] = listLeftHalf[i]
            i = i+1
            k = k+1
            intNumOfComp += 1
        while j < len(listRightHalf):
            argShuffledList[k] = listRightHalf[j]
            j = j+1
            k = k+1
            intNumOfComp += 1
    return argShuffledList, intNumOfComp


def insertion_sort(arr):
    counter = 0
    for i in range(1, len(arr), 1):
        j = i - 1
        b = arr[i]
        while( j > 0 and arr[j] > b):
            counter = counter + 1
            arr[j + 1] = arr[j]
            arr[j] = b
            j = j - 1
        counter = counter + 1
    return arr


def generate_data(n, gen_type="random"):
        a = [i + 1 for i in range(n)]
        random.shuffle(a)
        return a


for n in sizes:
    print("\nDATA SIZE: ", n)
    for gen_type in types:
        print("\n\tDATA TYPE:", gen_type)
        data = generate_data(n, gen_type)
        data_merge = np.copy(data)
        merge_op_count = MergeSort(data_merge)[1]
        print("\tMerge sort operation count:", merge_op_count)
        data_plot[gen_type]['merge'][n] = merge_op_count
        data_insertion = np.copy(data)
        insertion_op_count = insertion_sort(data_insertion)
        print("\tInsertion sort operation count:", int(insertion_op_count))
        data_plot[gen_type]['insertion'][n] = insertion_op_count


plot_data(data_plot, logarithmic=True, oneplot=True) #  Build a schedule
