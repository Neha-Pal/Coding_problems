def sum_dig(num):
    return sum(int(digit) for digit in str(num))

M,N = map(int, input().split())

sum_M = sum_dig(M)
sum_N = sum_dig(N)

reward = sum_M * sum_N

print(reward)