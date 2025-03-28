from heapq import heappop, heappush
from itertools import pairwise

class Solution:
    def maxPoints(self, points_grid: List[List[int]], queries: List[int]) -> List[int]:
        # Get the dimensions of the grid
        rows, cols = len(points_grid), len(points_grid[0])
      
        # Sort the queries along with their indices for efficient access
        sorted_queries = sorted((value, index) for index, value in enumerate(queries))
      
        # Initialize the answer list to have the same size as queries with default 0 values
        results = [0] * len(sorted_queries)
      
        # Initialize the priority queue with the starting point (0,0)
        priority_queue = [(points_grid[0][0], 0, 0)]
      
        # Counter to keep track of how many points have been visited
        points_count = 0
      
        # Initialize the visited matrix to track visited cells in the grid
        visited = [[False] * cols for _ in range(rows)]
        visited[0][0] = True
      
        # Iterate over the sorted queries
        for value, index in sorted_queries:
            # Process cells from the priority queue until the cell’s value is less than the query value
            while priority_queue and priority_queue[0][0] < value:
                # Pop the smallest value cell from the priority queue
                _, current_row, current_col = heappop(priority_queue)
              
                # Increment the visited points counter
                points_count += 1
              
                # Use the pairwise utility to iterate over the adjacent cells
                for delta_row, delta_col in pairwise((-1, 0, 1, 0, -1)):
                    # Calculate the adjacent cell's row and column
                    adjacent_row, adjacent_col = current_row + delta_row, current_col + delta_col
                  
                    # Check if the adjacent cell is inside the grid and not visited
                    if 0 <= adjacent_row < rows and 0 <= adjacent_col < cols and not visited[adjacent_row][adjacent_col]:
                        # Push the adjacent cell into the priority queue
                        heappush(priority_queue, (points_grid[adjacent_row][adjacent_col], adjacent_row, adjacent_col))
                      
                        # Mark the adjacent cell as visited
                        visited[adjacent_row][adjacent_col] = True
          
            # After processing the priority queue, assign the number of points visited to the results
            results[index] = points_count
      
        # Return the results list with the number of points visited for each query
        return results