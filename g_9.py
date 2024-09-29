# Given a string S, check if it is palindrome or not.

# Example 1:

# Input: S = "abba"
# Output: 1
# Explanation: S is a palindrome

class Solution:
    def isPalindrome(self, S):
        S_rev = S[::-1]
        if S == S_rev:
            return 1
        else:
            return 0
        ';]'
        
S='ABCA'
sol = Solution()
print(sol.isPalindrome(S))