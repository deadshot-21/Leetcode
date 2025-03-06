class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # The size of the grid is n*n.
        n = len(grid) 

        # Create a count array initialized with zeros, of size n*n + 1.
        # The extra 1 is to have an index equal to the maximum possible value in the grid.
        count = [0] * (n * n + 1)

        # Iterate over each row and each value in the grid, incrementing the corresponding count.
        for row in grid:
            for value in row:
                count[value] += 1

        # Initialize an answer list to store the repeated and missing values.
        answer = [0, 0] 

        # Go through the count array to find which value is repeated (count of 2)
        # and which is missing (count of 0).
        for i in range(1, n * n + 1):
            if count[i] == 2:
                answer[0] = i  # The repeated value.
            elif count[i] == 0:
                answer[1] = i  # The missing value.

        # Return the answer list containing the repeated and missing values.
        return answer