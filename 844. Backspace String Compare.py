"""
Approach:
We will use a 2 pointer approach starting one pointer at the end of each string each

We enter an inner loop which checks for '#' and processes them to do character skipping
If the pointer reaches a '#', we will increment a skip counter, which counts how many characters we need to discard. 
Then we keep running this loop until we don't see a '#' anymore and until all the characters that need to be skipped are handled. 

We iterate from the end of each string performing the skipping logic using the inner loop mentioned above. The iteration ends when one of the index reaches <= 0. We then return if the index are equal as our answer. Since the "skip check" for each string is done before the exit condition, it is guaranteed that the strings are not equal if the indexes are not equal after we exit the main iteration loop. 


Time complexity: O(n)
Space complexity: O(1)

"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        sp = len(s) - 1
        tp = len(t) - 1

        sSkip = 0
        tSkip = 0

        while sp >= 0 or tp >= 0:
            while sp >= 0 and (s[sp] == '#' or sSkip != 0):
                if s[sp] == '#':
                    sSkip += 1
                else:
                    sSkip -= 1
                sp -= 1
            
            while tp >= 0 and (t[tp] == '#' or tSkip != 0):
                if t[tp] == '#':
                    tSkip += 1
                else:
                    tSkip -= 1
                tp -= 1

            if sp < 0 or tp < 0:
                break
            elif s[sp] != t[tp]:
                return False

            sp -= 1
            tp -= 1

        return sp == tp
