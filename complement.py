# Given an array arr of size M and num. write a program to print the total number of unique pairs of integers in arr whose sum is equal to a given number num.
# sample input - 
# 4
# 2 2 4 5
# 6
# output - 6

M = int(input())
arr = list(map(int, input().split()))
num = int(input())


seen = set()
pair = set()

for i in arr:
    complement = num-i
    if complement in seen:
        pair.add(tuple(sorted((i, complement))))

    seen.add(i)

print(len(pair))