# Approach:
# Step 1: Count the frequencies of each character in the string
# Step 2: Initialize a set and iterate through each frequency and check if it is already in the set. If so, decrease the frequency and check again
class Solution:
    def minDeletions(self, s: str) -> int:
        freqs = [0] * 26
        # Count the char frequencies in the string
        for c in s:
            freqs[ord(c) - ord('a')] += 1

        ans = 0

        # Iterate through each set
        used_frequencies = set()
        for freq in freqs:
            while freq > 0 and freq in used_frequencies:
                freq -= 1
                ans += 1
            used_frequencies.add(freq)
            
        return ans
