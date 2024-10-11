# Given an array of strings arr. Return the longest common prefix among each and every strings present in the array. If there's no prefix common in all the strings, return "-1".

# Examples :

# Input: arr[] = ["geeksforgeeks", "geeks", "geek", "geezer"]
# Output: gee
# Explanation: "gee" is the longest common prefix in all the given strings.
# Input: arr[] = ["hello", "world"]
# Output: -1
# Explanation: There's no common prefix in the given strings.

class Solution():
    def findCommonPrefix(self,arr):
        if not arr:#if array is empty
            return -1
        
        prefix = arr[0]#Initialize the prefix as the 1st string
        for string in arr[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]#reduce the prefix until it matches to the beginning of the string
                if not prefix:
                    return -1
        return prefix
    
sol = Solution()
arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
print(sol.findCommonPrefix(arr))