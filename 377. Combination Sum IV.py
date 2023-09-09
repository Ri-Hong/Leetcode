class Solution:

    # Approach: DP
    # initialize an array called dp initially all 0, with dp[0] = 1 as the base case
    # dp[i] is the number of combinations for i
    # thus dp[target] will be the final answer we want
    # To populate the dp, loop through dp, and for each index, loop through each number in nums
    # If i - num >= 0, (meaning that the index i - num exists), then add dp[i - num] to dp[i]

    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]
