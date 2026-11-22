class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            # Shift from 1-indexed (1..26) to 0-indexed (0..25)
            columnNumber -= 1
            
            # Get the current rightmost letter
            remainder = columnNumber % 26
            result.append(chr(ord('A') + remainder))
            
            # Move to the next position to the left
            columnNumber //= 26

        # Reverse the collected letters since we built from right to left
        return "".join(reversed(result))
