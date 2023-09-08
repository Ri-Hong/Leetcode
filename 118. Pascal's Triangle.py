class Solution:
    # Approach:
    # Notice that each row begins and ends with 1
    # So for each row, we add 1 to the beginning and end. Then the numbers in the middle we can process by running a simple for loop through the previous row and adding the jth and j+1th numbers
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for i in range(numRows - 1):
            tempRow = [1]
            for j in range(i):
                tempRow.append(ans[i][j] + ans[i][j+1])
            tempRow.append(1)
            ans.append(tempRow)

        return ans
