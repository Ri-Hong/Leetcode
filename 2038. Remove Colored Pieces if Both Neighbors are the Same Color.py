# Approach
# We want to count the number of moves Alice and Bob can make respectively. Then we can compare these two results and find the answer
# We will use the sliding window and two pointer approach to count how many consecutive letters there are. We will perform a sliding window through each "segment" of conesecutive letters. 

# Time complexity: O(n) for sliding window
# Space complexity: O(1) for storing nAliceMoves and nBobMoves

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        nAliceMoves = nBobMoves = 0
        n = len(colors)

        left = right = 0

        while left < n:
            while right < n and colors[left] == colors[right]:
                right += 1
            
            if colors[left] == 'A':
                nAliceMoves += max(0, right - left - 2)
            else:
                nBobMoves += max(0, right - left - 2)

            left = right

        return True if nAliceMoves > nBobMoves else False
