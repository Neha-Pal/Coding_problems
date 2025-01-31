# Consider a string Str of lowercase alphabets. Write a program to find the resultant number which is formed by performing the below-given steps on Str:

# Step 1: For each letter ch of Str, if the ch is a vowel, the resultant binary string b must be concatenated with "0", else it is "1" and return the binary string b.

# Step 2: Print d, where d is the decimal equivalent of binary string b.
# input - zoo
#output - 4

def vowel_to_binary(s):
    # Step 1: Convert each character to binary based on vowel or consonant
    binary_string = ''.join('0' if ch in 'aeiou' else '1' for ch in s)
    
    # Step 2: Convert the binary string to a decimal number
    decimal_value = int(binary_string, 2)
    
    return decimal_value

# Input: a string of lowercase alphabets
s = input()

# Output: decimal equivalent of the binary string
print(vowel_to_binary(s))
