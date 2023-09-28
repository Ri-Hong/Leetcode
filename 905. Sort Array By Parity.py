# Approach:
# Step 1: Declare an array for the even numbers and odd numbers
# Step 2: Loop through nums and check if each number is even or odd and add it to the corresponding array
# Step 3: Return an array formed by joining the even and odd array

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for n in nums:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)

        return even + odd
