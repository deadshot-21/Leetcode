class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        heapq.heapify(heap)
        for n, cnt in count.items():
            heapq.heappush(heap,[cnt,n])
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]