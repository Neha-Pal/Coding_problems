# Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, act and tac are an anagram of each other. Strings a and b can only contain lowercase alphabets.

# Note:-

# If the strings are anagrams you have to return True or else return False

# |s| represents the length of string s.


# Example 1:

# Input:a = geeksforgeeks, b = forgeeksgeeks
# Output: YES
# Explanation: Both the string have same characters with same frequency. So, they are anagrams.
from collections import Counter
class Solution:
    def findAnagram(self, a, b):
        if len(a) != len(b):
            return
        count_a = Counter(a)
        count_b = Counter(b)
        return count_a == count_b

sol = Solution()
a = 'geeksforgeeks'
b = 'forgeeksgeeks'
print(sol.findAnagram(a,b))