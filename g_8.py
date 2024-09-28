# You are given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# If there are no such elements return an empty array. In this case, the output will be -1.

# Note: can you handle the duplicates without using any additional Data Structure?

# Examples :

# Input: arr1 = [1, 5, 10, 20, 40, 80] , arr2 = [6, 7, 20, 80, 100] , arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
# Output: [20, 80]
# Explanation: 20 and 80 are the only common elements in arr, brr and crr.
# Input: arr1 = [1, 2, 3, 4, 5] , arr2 = [6, 7] , arr3 = [8,9,10]
# Output: [-1]
# Explanation: There are no common elements in arr, brr and crr.

class Solution:
    def findCommen(self, arr1, arr2 ,arr3):
        i=0
        j=0
        k=0

        result = []

        while i<len(arr1) and j<len(arr2) and k<len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i+=1
                j+=1
                k+=1
            elif arr1[i]<arr2[j]:
                i+=1
            elif arr2[j]<arr3[k]:
                j+=1
            else:
                k+=1
        if not result:
            return [-1]
        else:
            return result
        
arr1 = [1, 5, 10, 20, 40, 80] 
arr2 = [6, 7, 20, 80, 100]  
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
sol = Solution()

print(sol.findCommen(arr1,arr2,arr3))