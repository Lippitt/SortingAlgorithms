# Binary Search Algorithm
# B Lippitt
# 08/09/2020

def binarySearch(arr, low, high, target): 
  
    while low <= high: 
  
        mid = low + (high - low) // 2; 
          
        # check target is midpoint
        if arr[mid] == target: 
            return mid 
  
        # if target is greater, ignore left half 
        elif arr[mid] < target: 
            low = mid + 1
  
        # if target is smaller, ignore right half 
        else: 
            high = mid - 1
      
    # return -1 if target not present in array
    return -1


arr = [ 2, 3, 4, 10, 40]
print('Array is: ',arr)
target = int(input('Enter target number: '))
low = 0
high = len(arr)-1

# call function and assign to variable
res = binarySearch(arr, low, high, target) 

print(target,'found at index:% d' % res) if res != -1 else print('Target not found')
