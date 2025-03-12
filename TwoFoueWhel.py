# Vehicle Manufacturing
# You are tasked with determining the number of two-wheelers and four-wheelers that need to be manufactured based on the given total number of vehicles and the total number of wheels.

# You are provided with two integers:

# v: the total number of vehicles (both two-wheelers and four-wheelers).
# w: the total number of wheels for all the vehicles combined.
# Your task is to calculate and print how many two-wheelers and four-wheelers must be manufactured based on the input data. If it's not possible to manufacture such a combination, print -1

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of two lines of input.
# The first line contains an integer v — the total number of vehicles.
# The second line contains an integer w — the total number of wheels.
# Output Format
# For each test case,

# If a valid combination of two-wheelers and four-wheelers exists, print two integers:
# The number of two-wheelers, the number of four-wheelers.
# If no valid combination is possible, print -1.

t = int(input())
for _ in range(t):
    v = int(input())
    w = int(input())

    if w % 2 != 0 or w < v*2 or w > v*4 or w < 2:
        print(-1)
    else:
        t_w = (v*4 - w) // 2
        f_w = v - t_w
        print(t_w, f_w)