# Given a string str without spaces, the task is to remove all duplicate characters from it, keeping only the first occurrence.

# Note: The original order of characters must be kept the same. 

# Examples :

# Input: str = "zvvo"
# Output: "zvo"
# Explanation: Only keep the first occurrence

class Solution():
    def removeDuplicate(self, str):
        seen = set()
        result = []
        for char in str:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return ''.join(result)
    
sol = Solution()
str = "zvvo"
print(sol.removeDuplicate(str))
