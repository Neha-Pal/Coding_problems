# Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
# For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

# Note: The driver code prints "balanced" if function return true, otherwise it prints "not balanced".
# Input: {([])}
# Output: true
# Explanation: { ( [ ] ) }. Same colored brackets can form balanced pairs, with 0 number of unbalanced bracket.
class Solution:
    def checkPar(self, x):
        # Stack to keep track of opening brackets
        stack = []
        # Dictionary for matching closing brackets to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in x:
            if char in bracket_map.values():  # Check if it's an opening bracket
                stack.append(char)  # Push it onto the stack
            elif char in bracket_map.keys():  # Check if it's a closing bracket
                # If stack is empty or the top of the stack does not match the closing bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False  # Unbalanced
                stack.pop()  # Pop the matching opening bracket
            else:
                return False  # Invalid character

        # If the stack is empty, all brackets matched; otherwise, unbalanced
        return len(stack) == 0

# Driver code
sol = Solution()
x = '(){}]'  # Example input

# Call the function and check the result
if sol.checkPar(x):  # Correctly call the function with the input
    print('Balanced')
else:
    print("Not Balanced")
