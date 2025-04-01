from typing import List
from functools import lru_cache  # Importing `lru_cache` for memoization

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Use lru_cache to memoize the recursive function results for efficiency
        @lru_cache(maxsize=None)
        def dfs(index: int) -> int:
            # Base case: If the index is beyond the questions list, no points can be earned
            if index >= len(questions):
                return 0
          
            # Unpack points (p) and bonus (b) from the current question
            points, bonus = questions[index]
          
            # Recursive case: Choose the maximum between two options:
            # 1. Earning points for the current question and jumping over the bonus questions
            # 2. Skipping the current question to try the next one
            return max(points + dfs(index + bonus + 1), dfs(index + 1))
      
        # Start the depth-first search from the first question (index 0)
        return dfs(0)