class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
    
        res=[intervals[0]]
        for start, end in intervals[1:]:
            prevE = res[-1][1]
            if start <= prevE:
                res[-1][1] = max(prevE,end)
            else:
                res.append([start,end])
        return res