# Write a program to find the maximum and minimum in a list.

def findMinMax(list):
    if list == 0:
        return None
    return min(list), max(list)

list = [9,7,0,23,5,-5]
print(findMinMax(list))
