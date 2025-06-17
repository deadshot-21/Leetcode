class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [[-count, char] for char, count in Counter(s).items()]
        heapq.heapify(heap)
        prev = None
        final_s = ""
        while prev or heap:

            if prev and not heap:
                return ""

            count, char = heapq.heappop(heap)
            final_s += char
            count+=1

            if prev:
                heapq.heappush(heap,prev)
                prev = None
            
            if count != 0:
                prev = [count,char]

        return final_s