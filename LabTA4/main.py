counter1 = 0
counter2 = 0
counter3 = 0


def threeelemsort(A, p, r):
    for k in range(p, r):
        if A[k + 1] < A[k]:
            A[k], A[k + 1] = A[k + 1], A[k]


def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)


def Partition(A, p, r):
    pivot = A[r]
    i = p-1
    j = p
    for j in range(j, r):
        global counter1
        counter1 = counter1+1
        if A[j] <= pivot:
            i = i+1
            A[i], A[j] = A[j], A[i]
        counter1 = counter1 + 1
    counter1 = counter1 + 1
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def QuickSortmod(A, p, r):
    if p < r and r-p > 3:
        q = Partitionmod(A, p, r)
        QuickSortmod(A, p, q-1)
        QuickSortmod(A, q+1, r)
    else:
        threeelemsort(A, p, r)
    threeelemsort(A, p, r)



def Partitionmod(A, p, r):
    arr = [A[p], A[(p+r)//2], A[r]]
    for k in range(0, 2):
        if arr[k+1] < arr[k]:
            arr[k], arr[k+1] = arr[k+1], arr[k]
    if arr[1] == A[p]:
        pivotpos = p
    elif arr[1] == A[(p+r)//2]:
        pivotpos = (p+r)//2
    else:
        pivotpos = r
    pivot = arr[1]
    i = p-1
    j = p
    A[pivotpos], A[r] = A[r], A[pivotpos]
    for j in range(j, r):
        global counter2
        counter2 = counter2+1
        if A[j] <= pivot:
            i = i+1
            A[i], A[j] = A[j], A[i]
        counter2 = counter2 + 1
    counter2 = counter2 + 1
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def QuickSortExtra(A, p, r):
    arr = [A[p], A[p + 1], A[r]]
    for k in range(0, 2):
        if arr[k + 1] < arr[k]:
            arr[k], arr[k + 1] = arr[k + 1], arr[k]
    A[p] = arr[0]
    A[p + 1] = arr[1]
    A[r] = arr[2]
    if p < r and r-p > 3:
        q = PartitionExtra(A, p, r)
        QuickSortExtra(A, p, q-1)
        QuickSortExtra(A, q+1, r)
    else:
        threeelemsort(A, p, r)
    threeelemsort(A, p, r)


def PartitionExtra(A, left, right):
    array = [A[left], A[left+1], A[right]]
    threeelemsort(array, 0, 2)
    A[left] = array[0]
    A[left+1] = array[1]
    A[right] = array[2]
    a = left+2
    b = left+2
    c = right-1
    d = right-1
    p = A[left]
    q = A[left+1]
    r = A[right]
    global counter3
    while b <= c:
        while A[b] < q and b <= c:
            counter3 = counter3+1
            if A[b] < p:
                A[a], A[b] = A[b], A[a]
                a = a+1
            b = b+1
            counter3 = counter3 + 1
        counter3 = counter3 + 1
        while A[c] > q and b <= c:
            counter3 = counter3 + 1
            if A[c] > r:
                A[c], A[d] = A[d], A[c]
                d = d-1
            counter3 = counter3 + 1
            c = c-1
        counter3 = counter3 + 1
        if b <= c:
            counter3 = counter3 + 1
            if A[b] > r:
                counter3 = counter3 + 1
                if A[c] < p:
                    A[b], A[a] = A[a], A[b]
                    A[a], A[c] = A[c], A[a]
                    a = a+1
                else:
                    A[b], A[c] = A[c], A[b]
            elif A[b] > r:
                A[c], A[d] = A[d], A[c]
                b = b+1
                c = c-1
                d = d-1
            else:
                counter3 = counter3 + 1
                if A[c] < p:
                    A[b], A[a] = A[a], A[b]
                    A[c], A[a] = A[a], A[c]
                    a = a+1
                else:
                    A[c], A[b] = A[b], A[c]
            b = b+1
            c = c -1
    a = a-1
    b = b-1
    c = c+1
    d = d+1
    A[left+1], A[a] = A[a], A[left+1]
    A[a], A[b] = A[b], A[a]
    a = a-1
    A[left], A[a] = A[a], A[left]
    A[right], A[d] = A[d], A[right]
    return c



def arraycopy(arrtocpy, arr, size):
    for i in range(size):
        arr.append(arrtocpy[i])


filename = input("Put the name of file you want to read: \n")
f = open(filename)
data = f.read()
f.close()
arr = []
arr = list(map(int, data.splitlines()))
n = arr[0]
del arr[0]
arr2 = []
arr3 = []
arraycopy(arr, arr2, n)
arraycopy(arr, arr3, n)
QuickSort(arr, 0, n-1)
QuickSortmod(arr2, 0, n-1)
QuickSortExtra(arr3, 0, n-1)
res = [counter1, counter2, counter3]
filename_res = open('is01_dankov_04_output.txt', 'w')
for i in range(0, 3):
    filename_res.write(str(res[i])+" ")


