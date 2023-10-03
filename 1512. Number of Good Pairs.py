# Approach: Triangular Numbers
'''
Step 1: Populate an occurance dictionary to count the number of occurances of each number
Step 2: Loop through each key in the dictionary and calculate the amount of good pairs there are for that key.
The key to this problem is to find the relationship between the # of numbers of each type and the amount of pairs it produces.
For example, the following is the table where the left column is the number of numbers of each type and the right column is the number of good pairs.

1 0
2 1
3 3
4 6
5 10
6 15
(i.e. If there is 1 number, there will be 0 good pairs. 2 numbers means 1 good pair. 3 numbers means 3 good pairs, etc.)

One may realize that the pattern formed is the triangular numbers. The forumla for the traingular numbers is n * (n-1)/2, where n is the first column in the above table. 


Time complexity: O(n) for traversing through nums and traversing through the occurance dictionary
Space complexity: O(n) for the occurance dictionary
'''

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        occ = {}

        for n in nums:
            occ[n] = occ.setdefault(n, 0) + 1

        ans = 0

        for n in occ.values():
            ans += n * (n - 1) // 2

        return ans
