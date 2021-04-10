import numpy as np


def InputMatrix(filename):  # Функція зчитування матриці вподобань з вхідного файлу
    inputfile = open(filename)  # Ініціалізація файлу з заданим ім'ям
    lst = []
    for line in inputfile:
        strs = line.split(' ')  # Розділення елементів кожного рядка
        for s in strs:
            if s != ' ':
                lst = lst + [int(s)]
    n = int(lst[0])         # Зчитування кількості користувачів
    k = int(lst[1])         # Зчитування кількості фільмів
    arr = np.zeros((n, k), dtype=int)  # Ініціалізація нульового масиву за допомогою бібліотеки NumPy
    t = 2
    for i in range(n):
        num = int(lst[t])
        t += 1
        for j in range(k):
            arr[i][j] = lst[t]  # Заповнення масиву пріоритетами
            t += 1
    inputfile.close()       # Завершення роботи з файлом
    return n, k, arr


def InputSorter(arr, x, n, k):  #  Функція сортування вхідного потоку даних
    for i in range(k):
        for j in range(k-i-1):  # improved bubble sort
            if arr[x][j] > arr[x][j+1]:
                for t in range(n):
                    arr[t][j], arr[t][j+1] = arr[t][j+1], arr[t][j]
    return arr


def SortAndCountInv(A):  #   Функція сортування та підрахунку інверсій (Див. псевдокод у лекції 3)
    n = len(A)
    if n == 1:
        return A, 0
    else:
        L = A[:int(len(A) / 2)]
        R = A[int(len(A) / 2):]
        L, x = SortAndCountInv(L)
        R, y = SortAndCountInv(R)
        A, z = MergeAndCountSplitInv(A, L, R)
        return A, x + y + z


def MergeAndCountSplitInv(A, L, R):   #   Функція злиття та підрахунку розділених інверсій (Див. псевдокод у лекції 3)
    c = []
    i = 0
    j = 0
    z = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            c.append(L[i])
            i += 1
        else:
            c.append(R[j])
            j += 1
            z += (len(L) - i)
    c = c + L[i:]
    c = c + R[j:]
    return c, z


def OutputSorter(result, n):        #  Функція сортування вихідного потоку даних
    for i in range(n):
        for j in range(n - i - 1):  # improved bubble sort
            if result[j][1] > result[j + 1][1]:
                result[j][1], result[j + 1][1] = result[j + 1][1], result[j][1]
                result[j][0], result[j + 1][0] = result[j + 1][0], result[j][0]
    return result


def Output(result, x, n):            #  Функція утворення вихідного файлу
    outputfile = open("output.txt", 'wt')
    x += 1
    s = str(x) + '\n'
    outputfile.write(s)
    for i in range(1, n):
        s1 = str(result[i][0])
        s2 = str(result[i][1])
        outputfile.write(s1 + ' ' + s2 + '\n')



def InvCounter(arr, x, n, k):        #  Повна процедура підрахунку інверсій
    arr = InputSorter(arr, x, n, k)
    result = np.zeros((n, 2), dtype=int)
    t = 0
    for i in range(n):
        if i != x:
            t += 1
            result[t][0] = i+1
            mas = arr[i]
            A, result[t][1] = SortAndCountInv(list(mas))
    result = OutputSorter(result, n)
    Output(result, x, n)


file = str(input("Put the name of input file below: \n"))
n, k, arr = InputMatrix(file)
index = int(input("Put the index of person to compare: \n ")) - 1
InvCounter(arr, index, n, k)
