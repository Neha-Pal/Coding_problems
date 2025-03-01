# Union of Sorted Arrays
# You are given two sorted arrays, arr1 and arr2 of size N and M respectively.

# Your you have to find the union of these two arrays. The union of two arrays is a sorted array that contains all the distinct elements from both the arrays. The union should also be sorted.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of two lines of input:
# The first line contains two integers N and M, denoting the size of arr1 and arr2 respectively.
# The second line contains N space-separated integers, denoting the elements of arr1.
# The third line contains M space-separated integers, denoting the elements of arr2.

# Output Format
# For each test case, output a sorted array containing the distinct elements from both the arrays.
# Input:
# 2
# 5 4
# 1 3 4 5 7
# 2 3 5 10
# 3 2
# 11 12 13 
# 14 25 
# Output:
# 1 2 3 4 5 7 10
# 11 12 13 14 25

def unionOfArrays(m, n, arr1, arr2):
    arr = sorted(set(arr1 + arr2))
    return arr
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, n = map(int, input().split())
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))

        result = unionOfArrays(m, n, arr1, arr2)
        print(*result)