class Solution:
    def remove_duplicate(self, arr):
        #Code Here
        seen = set()
        result = []
        for num in arr:
            if num not in seen:
                result.append(num)
                seen.add(num)
        return result
    
arr = [2,2,2,2,2,3]
sol = Solution()
print(sol.remove_duplicate(arr))