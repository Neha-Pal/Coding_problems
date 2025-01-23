# Given a list L of N numbers, print the sum S of all the checksums of the list after eliminating the minimum and maximum digits from each number's checksum.

# Where:

# Checksum: The sum of all the digits of a number.
# Elimination: For each number in the list, remove the minimum and maximum digits from its checksum.
# Special Case: If eliminating the minimum and maximum digits leaves no digits remaining, the number's checksum is considered 0.

# Input - 
# 4
# 1223 234 3445 456
# output - 20

def calculate_checksum(num):
    # Convert the number to a list of its digits
    digits = [int(d) for d in str(num)]
    
    # Remove the minimum and maximum digits
    if len(digits) > 2:
        digits.remove(min(digits))
        digits.remove(max(digits))
        return sum(digits)
    else:
        # If no digits remain after removal, checksum is 0
        return 0

# Input: number of elements
n = int(input())
# Input: list of numbers
numbers = list(map(int, input().split()))

# Compute the total checksum
total_checksum = sum(calculate_checksum(num) for num in numbers)

# Output the result
print(total_checksum)
