# Approach:
# Step 1: Create an arary of length 26, storing the occurances of each letter. note that this can be a hashmap too
# Step 2: Iterate thorugh s and update the array, adding 1 for each character
# Step 3: Iterate thorugh t and update the array again, this time subtracting 1 for each character. If one of the occurance indexes is 0 before subtracting, then that is the answer. 
# Note: To optimize it a bit, we can check for the answer after the array has been update for the second time. This way, we don't need to check for 0 for every single character in t

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        occurances = [0] * 26

        for c in s:
            occurances[ord(c) - ord('a')] += 1
        
        for c in t:
            occurances[ord(c) - ord('a')] -= 1
        
        for i, num in enumerate(occurances):
            if num == -1:
                return chr(i + ord('a'))
