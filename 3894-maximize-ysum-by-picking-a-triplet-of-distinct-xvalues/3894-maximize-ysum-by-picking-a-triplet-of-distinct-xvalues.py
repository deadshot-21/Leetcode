class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        
        x_y = defaultdict(list)

        for i in range(len(x)):
            x_y[x[i]].append(y[i])
        
        cand = []

        for x_val, y_list in x_y.items():
            cand.append((max(y_list),x_val))
        
        cand.sort(key = lambda x: x[0], reverse=True)

        if len(cand) < 3:
            return -1
        
        return cand[0][0]+cand[1][0]+cand[2][0]