from collections import defaultdict

class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        
        n = len(x)
        
        x_to_y_values = defaultdict(list)
        for i in range(n):
            x_to_y_values[x[i]].append(y[i])

        candidates = []
        for x_val, y_list in x_to_y_values.items():
            candidates.append((max(y_list), x_val))
        
        candidates.sort(key=lambda item: item[0], reverse=True)

        if len(candidates) < 3:
            return -1

        max_sum = candidates[0][0] + candidates[1][0] + candidates[2][0]

        return max_sum
        
                