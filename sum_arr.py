def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

arr = list(map(int, input().split()))
print(sum(arr))