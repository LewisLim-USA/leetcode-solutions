# Last updated: 6/25/2025, 4:09:43 AM
from heapq import heappush, heappop, heapify
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # \U0001f4ca Real-life context:
        # Imagine you're monitoring a stream of scores, prices, or sales.
        # You want to continuously track the "k-th highest" (e.g., top 5 product sales).
        
        self.k = k
        self.min_heap = nums  # We'll use a min-heap to keep track of the top k elements

        # \U0001f527 Convert the initial list into a heap in-place
        heapify(self.min_heap)

        # \U0001f9f9 Keep only the k largest elements in the heap
        while len(self.min_heap) > k:
            heappop(self.min_heap)  # Remove smallest of the top elements

    def add(self, val: int) -> int:
        # \U0001f504 A new value arrives in the stream (like a new sale, new score, new follower count)
        heappush(self.min_heap, val)

        # \U0001f9f9 If we exceed k elements, remove the smallest (we only want the top k!)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)

        # \U0001f3af The smallest in the heap is now the k-th largest overall
        return self.min_heap[0]
