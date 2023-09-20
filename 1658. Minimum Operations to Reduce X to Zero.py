# Approach:
# Step 1: Compute the sum of nums. Subtract x from it. Call this total sum_target. This is the sum of the remaining numbers in nums that we need to achieve
# Step 2: Perform sliding window using 2 pointers to find a subarray that sums up to sum_target. 

# Note: we need to find the *minimum* number of operations, not just any. Thus, we cannot simply return as soon as we find a valid subarray. We must store all our valid subarrays and return the one that results in the least # of operations. This can be optimized using a variable called min_operations

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sum_target = sum(nums) - x

        left = 0
        c_sum = 0

        min_operations = float('inf')

        for right in range(len(nums)):
            c_sum += nums[right]
            
            while c_sum > sum_target and left <= right:
                c_sum -= nums[left]
                left += 1

            if c_sum == sum_target:
                min_operations = min(min_operations, len(nums) - (right - left + 1))
        
        if min_operations == float('inf'):
            return -1
        else:
            return min_operations
