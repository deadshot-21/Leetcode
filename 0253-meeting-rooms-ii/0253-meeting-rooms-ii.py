class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        count, res = 0, 0
        s,e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s+=1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res,count)
        return res
            