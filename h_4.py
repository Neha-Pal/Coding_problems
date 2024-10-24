# Min-Max sum
# example--
# arr = [1,3,5,7,9]
# out = 16 24

# minsum = 1+3+5+7=16
# max_sum = 3+5+7+9 = 24
import math
def findMinMax(arr):
    arr.sort()
    n = len(arr)
    min_sum = sum(arr[:n-1])
    max_sum = sum(arr[1:])
    print(min_sum, end = ' ')
    print(max_sum)

    
arr = [1,3,5,7,9]
print(findMinMax(arr))