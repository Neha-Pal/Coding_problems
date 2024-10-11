# Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. If there is no non-repeating character, return '$'.

# Note: When you return '$' driver code will output -1.

# Examples:

# Input: s = hello
# Output: h
# Explanation: In the given string, the first character which is non-repeating is h, as it appears first and there is no other 'h' in the string.

class Solution():
    def repeatingChar(self, s):

        frequency = {}
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        for char in s:
            if frequency[char] == 1:
                return char
        return '$'
    
sol = Solution()
s = 'hello'
print(sol.repeatingChar(s))
