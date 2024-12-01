# N number of the army is waiting to enter a Castle. At a time 10 people can enter the Castle.

# ➢ You have to make a function that will return a list of the N people. Where the length of the
# inner list is 10.
# Test Case: Input N = 100, Output = [[1,2,3,4,5....,9,10], [11, 12...],. [....,100]]

def group_army(N):
    groups = []
    for i in range(1, N + 1, 10):
        groups.append(list(range(i, min(i + 10, N + 1))))
    return groups

N = 100
output = group_army(N)
print(output)
