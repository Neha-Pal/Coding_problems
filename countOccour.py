# Problem statement: Given an array, we have found the number of occurrences of each element in the array.
# Example 1:
# Input: arr[] = {10,5,10,15,10,5};
# Output: 10  3
# 	    5  2
#         15  1

def countOccour(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

arr = list(map(int, input().split()))
print(countOccour(arr))