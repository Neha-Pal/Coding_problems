# Problem Statement: You are given an array. The task is to reverse the array and print it. 

def reverseArr(arr):
    return arr[:: -1]

arr = list(map(int, input().split()))
print(reverseArr(arr))