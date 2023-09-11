# Approach:
# Step 1: Store each person in a hashmap, where the key is the groupsize and the value is the person's index

# Step 2: Go through each groupsize in the hashmap and create the groups

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hm = {}
        ans = []

        # Step 1
        for i in range(len(groupSizes)):
            hm.setdefault(groupSizes[i], []).append(i )

        # Step 2
        for groupSize, people in hm.items():
            temp = []
            for person in people:
                temp.append(person)
                if len(temp) == groupSize:
                    ans.append(temp)
                    temp = []
        
        return ans
        