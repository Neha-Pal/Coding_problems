# bubble_sort

class Solution():
    def bubbleSort(self, arr):
        for i in range(len(arr)):
            swapped = False

            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
        
sol = Solution()
arr = [90,34,11,56,67]
print(sol.bubbleSort(arr))

