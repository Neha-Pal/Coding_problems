# Longest Common Prefix
# You are given a list of strings str
# str. Your task is to find the longest common prefix among all the strings in the list. If there is no common prefix, return -1

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of two lines of input:
# The first line contains an integer N, the number of strings.
# The next line contain a string array str.
# Output Format
# For each test case, output the longest common prefix. If there is no common prefix, output -1

t = int(input())
for _ in range(t):
    n = int(int(input()))
    str = input().strip().split()

    if not str:
        print("-1")
        continue

    str.sort()
    first = str[0]
    last = str[1]

    prefix = []
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            prefix.append(first[i])
        else:
            break
    if prefix:
        print(''.join(prefix))
    else:
        print(-1)