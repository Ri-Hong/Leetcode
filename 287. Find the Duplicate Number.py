# Approach:
# Step 1: Sort the array: O(nlogn)
# Step 2: Perform a binary search through the sorted array to find the duplicate

# Time complexity: O(nlogn)
# Space complexity: O(n)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        new = sorted(nums)

        left = 0
        right = len(nums) - 1

        while new[left] != new[right]:
            center = (left + right) // 2

            if new[center] - 1 >= center:
                left = center
            else:
                right = center

        return new[left]
