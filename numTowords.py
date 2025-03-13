# Convert number to words
# You are tasked with creating a program that converts a given integer (up to 4 digits) into its corresponding English words.

# Input Format
# First line of input contains a single integer T, the number of test cases.
# Each test case consists of a single line containing a number N.
# Output Format
# For each test case, output the number in words, following the English naming conventions. Each number should be converted to its corresponding words in lowercase, with words separated by a single space.
# Input - 
# 2
# 7824
# 378

# Output -
# seven thousand eight hundred twenty four
# three hundred seventy eight

def numToWords(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens =  ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen"]
    tens = ["", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninty"]
    words = []
    if n==0:
        return "zero"
    if n >= 1000:
        words.append(ones[n // 1000] + " thousand")
        n %= 1000

    if n >= 100:
        words.append(ones[n // 100] + " hundred")
        n %= 100
    
    if n >= 20:
        words.append(tens[n // 10])
        n %= 10
    
    if 10 <= n < 20:
        words.append(teens[n - 10])
        n = 0
    
    if n > 0:
        words.append(ones[n])

    return " ".join(words).strip()

T = int(input())
for _ in range(T):
    n = int(input())
    print(numToWords(n))    
