# Given an array arr, return the second largest distinct element from an array. If the second largest element doesn't exist then return -1.
# Input: arr = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
# Input: arr = [10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist so answer is -1.

class Solution:
    def secondLargest(self, arr):
        # convert the arr into a set to remove duplicates
        arr_set = list(set(arr))

        if len(arr_set) < 2:
            return -1
        #sort the set in decensing order

        arr_set.sort(reverse=True)
        return arr_set[1]
sol = Solution()
n=5,
arr = [10,10]
print(sol.secondLargest(arr))


n=6,
arr = [1,4,11,10,3,6]
print(sol.secondLargest(arr))
