# Approach
# Step 1: Use the python split() function to split the string by spaces.
# Step 2: Travsere through each word, reverse it, and add it to the answer array, making sure to add a space after each word.
# Step 3: Return answer, but without the last character (as that is an extra space)

# Time complexity: O(n)
# Space complesity: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")

        ans = []

        for word in words:
            ans.append(word[::-1] + " ")

        return ''.join(ans)[0:-1]
