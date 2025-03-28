# Given a numerical array with n values from 0 to 9, find the smallest possible sum S (represented as a string) of two numbers created using the digits of the array elements. The two numbers together should include all the digits of the array. 
# input - 
# 6
# 6 8 5 4 2 3
# output - 604

def smallest_sum(arr):
    # Step 1: Sort the array to arrange digits in ascending order
    arr.sort()
    
    # Step 2: Distribute digits into two numbers in an alternating manner
    num1, num2 = "", ""
    for i in range(len(arr)):
        if i % 2 == 0:
            num1 += str(arr[i])  # Add digit to the first number
        else:
            num2 += str(arr[i])  # Add digit to the second number
    
    # Step 3: Convert strings to integers, add them, and return the result
    return int(num1) + int(num2)

# Input
n = int(input())  # Number of digits
arr = list(map(int, input().split()))  # Array of digits

# Output
print(smallest_sum(arr))
