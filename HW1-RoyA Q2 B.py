#Adam Roy CSCI 242 HW 1 Problem 2 B

def assignArray():
    array = [84, 64, 24, 14, 54, 34, 4, 44, 74]
    return array

def findMin(A, n):
    i = 0
    a = 10000
    if (n == 1):
        return A[0]
    else:
        for i in range(0, (n - 1)):
            if (A[i] < a):
                a = A[i]
        return a

def findMax(A, n):
    i = 0
    b = 0
    if (n == 1):
        return A[0]
    else:
        for i in range(0, (n - 1)):
            if (A[i] > b):
                b = A[i]
        return b

def main():
    array = assignArray()
    n = len(array)
    a = findMin(array, n)
    b = findMax(array, n)
    print("Minimum =", a, "\nMaximum =", b)

main()
