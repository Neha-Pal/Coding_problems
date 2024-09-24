# Given an array arr of size n which contains elements in range from 0 to n-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order. If no such element is found, return list containing [-1]. 
# Input: n = 4, arr[] = [0,3,1,2]
# Output: -1
# Explanation: There is no repeating element in the array. Therefore output is -1.
# Input: n = 5, arr[] = [2,3,1,2,3]
# Output: 2 3 
# Explanation: 2 and 3 occur more than once in the given array.

class Solution():
    def duplicate_num(self, n, arr):  # Add 'self' as the first parameter
        frequency = {}
        result = []

        # Count the frequency of each number in the array
        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        # Append numbers that occur more than once to the result list
        for key, value in frequency.items():
            if value > 1:
                result.append(key)
        
        # Return [-1] if no duplicates are found
        if len(result) == 0:
            return [-1]
        else:
            result.sort()  # Ensure the result is in ascending order
            return result


n = 5
arr = [2, 3, 1, 2, 4]

sol = Solution()
print(sol.duplicate_num(n, arr))  # Output: [2]
