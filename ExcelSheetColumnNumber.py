class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            # Calculate the value of the current character
            value = ord(char) - ord('A') + 1
            # Shift the current result to the left by multiplying by 26 and add the value of the current character
            result = result * 26 + value
        return result