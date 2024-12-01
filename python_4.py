# Make a function, that will take a number of more than 2 digits and return the sum of all digits.

# Test Case: Input: 100 => Output: 1
# Input: 204=> Output: 6
# Input: 333=> Output: 9

def sum_of_digits(num):
    str_num = str(num)
    list = []
    for i in str_num:
        list.append(int(i))
    return sum(list)
    
n = 204
print(sum_of_digits(n))