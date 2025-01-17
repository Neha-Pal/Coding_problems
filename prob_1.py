# A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array  of N number of integer values. The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).

# Example 1 :

# N=8 and arr = [4,5,0,1,9,0,5,0].

# There are 3 empty packets in the given set. These 3 empty packets represented as O should be pushed towards the end of the array

# Input :

# 8  – Value of N

# [4,5,0,1,9,0,5,0] – Element of arr[O] to arr[N-1],While input each element is separated by newline

# Output:

# 4 5 1 9 5 0 0 0

n = int(input())  # Input the size of the list
L = list(map(int, input().split()))  # Input the list of integers

j = 0
# Move non-zero elements to the front
for i in range(n):
    if L[i] != 0:
        L[j] = L[i]
        j += 1

# Fill the remaining elements with zeros
for i in range(j, n):
    L[i] = 0

print(L)

