# Approach:
# Step 1: Setup two variables, mInc and mDec (assumed to be initially true) to track whether the array is monotone increasing or monotone decreasing.
# Step 2: Iterate through the array, checking and updaing mDec and mInc by looking at the current and next elements in nums.
# Step 3: If during the iteration, mInc and mDec are both false, then we can return false. If the loop finishes without returning, then we return true. 

# Time Complexity: O(n)
# Space Complexity:  O(1)

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        mInc = mDec = True

        for i in range(len(nums) - 1):
            if nums[i+1] > nums[i]:
                mDec = False
            
            elif nums[i+1] < nums[i]:
                mInc = False
            
            if not (mDec or mInc):
                return False
        
        return True
