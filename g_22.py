# You are given an array a, of n elements. Find the minimum index based distance between two distinct elements of the array, x and y. Return -1, if either x or y does not exist in the array.

# Example 1:

# Input:
# N = 4
# A[] = {1,2,3,2}
# x = 1, y = 2
# Output: 1
# Explanation: x = 1 and y = 2. There are
# two distances between x and y, which are
# 1 and 3 out of which the least is 1.

class Solution():
    def calculateDistance(self,arr,n,x,y):
        index_x = -1
        index_y = -1
        distance = float('inf')

        for i in range(n):
            if arr[i] == x:
                index_x = i
            elif arr[i] == y:
                index_y = i
            
            if index_x != -1 and index_y != -1:
                distance = min(distance, abs(index_x - index_y))

        if index_x == -1 or index_y == -1:
            return -1
        
        return distance
    
sol = Solution()
n = 4
A = [1,2,3,2]
x = 1
y = 2

print(sol.calculateDistance(A,n,x,y))