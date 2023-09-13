# Approach: Two pass greedy

# Step 1: Initialize an array of length len(ratings) and set it all to 1s, because every child needs at least one candy. Call this array candy and it represents the amount of candy each child should receive

# Step 2: "Look to the left"
# Iterate through candies from left to right, checking if the current rating is greater than the one to the left, if it is, update the candy array to have one more candy than the left person.

# Step 3: "Look to the right"
# Similarly to step 2, iterate from right to left, checking the candy to the right this time. Check if the current rating is greater than the one to the right. 
# However, we update the current candy index to be the MAX of the current candy index and one more than the candy amount of the index to our right (in other words, max(candies[i], candies[i+1] + 1)). 

# We take thie max because this candies[i] might have been updated in our first pass, and if we don't consider candies[i], it could potentially get set to a lower number, and thus it would not satisfy "Look to the left", where it could potentially have a lower amount of candy while the idnex on the left has a higher rating

# Note: the reason we look to the left when moving right is because this way, we can assume the left side to be "set" as we pass thorugh it. Similar logic for looking to the right when moving left.

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        # Moving left to right, left side is "set"
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # Moving right to left, right side is "set"
        for i in reversed(range(0, len(ratings)-1)):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)
