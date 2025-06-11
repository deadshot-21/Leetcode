from collections import defaultdict

class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        
        n = len(x)
        # 1. Group y values by x values
        # x_to_y_values: {x_val: [y_val1, y_val2, ...]}
        x_to_y_values = defaultdict(list)
        for i in range(n):
            x_to_y_values[x[i]].append(y[i])

        # 2. For each x value, find its maximum y value
        # This implicitly handles the distinct indices for the same x value,
        # by only considering the highest y for a given x.
        # This is correct because if we pick x[i] and x[k] where x[i] == x[k]
        # and y[i] > y[k], we would always prefer y[i].
        
        # candidates: [(max_y_for_x_val, x_val)]
        candidates = []
        for x_val, y_list in x_to_y_values.items():
            # Get the maximum y value for the current x_val
            candidates.append((max(y_list), x_val))
        
        # 3. Sort candidates by y value in descending order
        # This ensures we pick the largest y values first.
        candidates.sort(key=lambda item: item[0], reverse=True)

        # 4. Check if we have at least three distinct x values
        # If len(candidates) < 3, it means there are fewer than 3 unique x values,
        # making it impossible to pick a triplet of distinct x values.
        if len(candidates) < 3:
            return -1

        # 5. The maximum sum will be the sum of the top 3 y values from the sorted candidates.
        # Since each candidate represents a unique x value (with its max y),
        # picking the top 3 guarantees distinct x values.
        max_sum = candidates[0][0] + candidates[1][0] + candidates[2][0]

        return max_sum
        
                