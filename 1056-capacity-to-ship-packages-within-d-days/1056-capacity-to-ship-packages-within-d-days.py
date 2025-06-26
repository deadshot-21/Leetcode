class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        def feasible(capacity):
            days_needed = 1
            current = 0
            for w in weights:
                if current + w <= capacity:
                    current += w
                else:
                    days_needed += 1
                    current = w
            return days_needed <= days
        
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        
        return low

