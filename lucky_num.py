# Mr. Rock on his way to the office used to observe a board, where a lucky number S of that day is written. It was written by an older man to build some interest in math among the office employees. Every day he used to note the numbers in his dairy.

#  1  He did a lot of math on it and found that if he takes the last N numbers in sequence, then the lucky number is equal to the sum of all the numbers that have repeated an odd number of times.
# sample input-1
# 7
# 11 11 12 12 13 13 13
# output - 39
# sample input-2
# 5
# 100 200 300 40 40
# output - 600
def lucky_number(sequence):
    # Dictionary to store frequency of each number
    frequency = {}
    
    # Count occurrences of each number
    for num in sequence:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Calculate the sum of numbers with an odd frequency, multiplied by their frequency
    lucky_sum = 0
    for num, count in frequency.items():
        if count % 2 != 0:  # Odd frequency
            lucky_sum += num * count  # Add number multiplied by its frequency
    
    return lucky_sum


# Input
n = int(input("Enter the number of elements: "))  # Number of elements
sequence = list(map(int, input("Enter the sequence: ").split()))  # List of numbers

# Ensure the length of the sequence matches the input count
if len(sequence) != n:
    print("The number of elements in the sequence does not match the input count.")
else:
    # Output
    print("Lucky Number:", lucky_number(sequence))
