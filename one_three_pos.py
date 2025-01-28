# The first line of integers contains an integer k , the size of the array . the second line of input should consist of N integers.
# sample input - 
# 8
# 28 24 21 4 26 28 4 5
# output
# 28 21 26 4

k = int(input())
n = list(map(int, input().split())) #array

result = []
for i in range(k):
    if i%2 == 0:
        result.append(n[i])
print(result)