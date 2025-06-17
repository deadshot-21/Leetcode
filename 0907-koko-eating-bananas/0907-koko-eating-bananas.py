class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        possible_values = [i for i in range(1,max(piles)+1)]
        l,r = 0, len(possible_values) - 1
        while l<=r:
            m = (l+r) // 2
            no_of_h = 0
            for p in piles:
                no_of_h += math.ceil(p/possible_values[m])
            print(no_of_h)
            if no_of_h > h:
                l = m + 1
            elif no_of_h < h:
                r = m - 1
            else:
                return possible_values[m]