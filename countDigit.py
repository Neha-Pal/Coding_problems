# Problem statement
# You are given a number ’n’.



# Find the number of digits of ‘n’ that evenly divide ‘n’.



# Note:
# A digit evenly divides ‘n’ if it leaves no remainder when dividing ‘n’.


# Example:
# Input: ‘n’ = 336

# Output: 3

def couDigit(n:int)->int:
    count = 0
    value = n
    n = abs(n)

    for i in str(n):
        i = int(i)
        if i != 0 and value % i == 0:
            count += 1
    return count
n = 336
print(couDigit(n))