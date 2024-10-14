# Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating (in any direction) string 'a' by exactly 2 places.

# Example 1:

# Input:
# a = amazon
# b = azonam
# Output: 
# 1
# Explanation: 
# amazon can be rotated anti-clockwise by two places, which will make it as azonam.
# Example 2:

# Input:
# a = geeksforgeeks
# b = geeksgeeksfor
# Output: 
# 0
# Explanation: 
# If we rotate geeksforgeeks by two place in any direction, we won't get geeksgeeksfor.

class Solution():
    def isRotated(self, str1, str2):
        if len(str1) != len(str2):
            return 0
        
        clockwise_rotate = str1[-2:] + str1[:-2]
        anticlockwise_rotate = str1[2:] + str1[:2]

        if str2 == clockwise_rotate or str2 == anticlockwise_rotate:
            return 1
        
        return 0
sol = Solution()   
a = 'amazon'
b = 'azonam'
print(sol.isRotated(a, b))