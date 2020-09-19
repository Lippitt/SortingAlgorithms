# Fibonacci Search
# B Lippitt
# 08/09/2020

# imports
from bisect import bisect_left

# fib search function
def fibSearch(arr, target, n):
    #init fib numbers
    fib_minus_2 = 0 # m-2'th fib no.
    fib_minus_1 = 1 # m-1'th fib no.
    fib_no = fib_minus_2 + fib_minus_1 # m'th fib no.

    # increment fib numbers
    while(fib_no < n):
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib_no
        fib_no = fib_minus_2 + fib_minus_1

    offset = -1

    #while there are elements in list to check
    while(fib_no > 1):
        # check fib_minus_2 is at valid point
        i = min(offset+fib_minus_2, n-1)

        # check if target value is greater than index fib_minus_2
        # if so, cut array from offset to i
        if(arr[i] < target):
            fib_no = fib_minus_1
            fib_minus_1 = fib_minus_2
            fib_minus_2 = fib_no - fib_minus_1
            offset = i

        # check if target is less than index fib_minus_2
        # if so, cut array from position i+1
        elif(arr[i] > target):
            fib_no = fib_minus_2
            fib_minus_1 = fib_minus_1 - fib_minus_2
            fib_minus_2 = fib_no - fib_minus_1

        #element is found, return position
        else:
            return i

    # check to compare last element with target
    if(fib_minus_1 and arr[offset+1] == target):
        return offset+1;

    return -1


arr = [34,4,65,6,32,5,8,354,67,233,5467]
n = len(arr)
print('Array is:',arr)
target = int(input('Enter target value: '))
print(fibSearch(arr,target,n))
    
