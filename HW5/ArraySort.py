#Adam Roy
#CSCI 242
#Assignment 5

def createUnsort(size):
    i=0
    unsort = []
    for i in range(0, size): #this runs on f(n) time
        unsort.append(-1)
    return unsort

def sortArr(MyArray, size):
    i=0
    unsort = createUnsort(size)
    for i in range(0, len(MyArray)): #this runs on f(n) time
        if MyArray[i] != (-1):
            unsort[MyArray[i]] = MyArray[i]
    return unsort

def main(): #this entire function runs on linear time
    MyArray1 = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    MyArray2 = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
    run = sortArr(MyArray1, len(MyArray1))
    print(run)
    run = sortArr(MyArray2, len(MyArray2))
    print(run)
main()

"""
PSUDOCODE
intialize each function of the code
send the size of array to function to create array of -1's named "arrB"
by entering a for loop and appending the number -1 to the array until
it reaches the end of the for condition
following the create unsort function the input array and the "arrB"
are sent to the sort function, within the sort function there is a for loop.
Within the for loop if the element in the input array is not equal to -1
then the number in the input array is determined to be the index location in "arrB"
the sort function then goes to the index location the changes the -1 in the location
to the number in the input array.
after the process is complete the printed array is sorted
"""
"""
TIME COMPLEXITY
this function runs on O(n) time it is calculated by taking each piece of the function and
adding their times together
f(n) + f(n) + f(1) = f(2n + 1)
after taking aseptotic analysis on the function it would equal
f(n) which is equal to O(n)
indicating that the function runs on O(n) time.
"""