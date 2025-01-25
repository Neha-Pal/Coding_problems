# Here's the question based on the provided image:

# Question:

# Problem Statement:

# A game has acquired a lot of popularity in a circle, with young children playing with a circular game board.

# Game Description:

# The game involves N kids standing in a circle. Each child is assigned a unique position numbered from 1 to N. The game starts with the kid at position 1. The game proceeds in a clockwise direction. In each round, the current kid will skip the next X kids and eliminate the one after that. The process continues until only one kid remains.

# Task:

# You need to find the position of the kid who will be the last one standing after X passes in the clockwise direction.

# Input Format:

# The first line of the input contains two integers, N and X, where N denotes the number of kids who have participated in the game and X denotes the number of passes in each round.

# Output Format:

# The one and only line of output contains an integer, the position of the last kid left after making X passes in the clockwise direction.

# Sample Input:

# 10 15

# Sample Output:

# 6

# Explanation:

# In the first round, the kid at position 1 will skip the next 15 kids (positions 2 to 16) and eliminate the kid at position 17. The game continues in this manner until only one kid remains. The last kid standing will be at position 6.

def find_last_kid_standing(N, X):
    # Initialize position to 0 (0-based index)
    position = 0
    # Simulate the elimination process
    for i in range(1, N + 1):  # Loop from 1 to N
        position = (position + X) % i

    # Convert 0-based index to 1-based index for the final answer
    return position + 1

# Input
N, X = map(int, input("Enter N and X: ").split())

# Output the result
print(find_last_kid_standing(N, X))

