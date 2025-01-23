# int findCount(int arr[], int length, int num, int diff);

# The function accepts an integer array ‘arr’, its length and two integer variables ‘num’ and ‘diff’. Implement this function to find and return the number of elements of ‘arr’ having an absolute difference of less than or equal to ‘diff’ with ‘num’.
# Note: In case there is no element in ‘arr’ whose absolute difference with ‘num’ is less than or equal to ‘diff’, return -1.

# Example:
# Input:

# arr: 12 3 14 56 77 13
# num: 13
# diff: 2
# Output:
# 3
def findCount(n, arr, num, diff):
    count = 0
    for i in range(n):
        if abs(arr[i] - num) <= diff:
            count += 1
    return count

# Input: Number of elements in the array
n = int(input())  # First input is the number of elements

# Input: Array elements as space-separated integers
arr = list(map(int, input().split()))  # Second input is the space-separated array

# Input: num and diff values
num = int(input())  # Third input is num
diff = int(input())  # Fourth input is diff

# Output: Call the function and print the result
print(findCount(n, arr, num, diff))
