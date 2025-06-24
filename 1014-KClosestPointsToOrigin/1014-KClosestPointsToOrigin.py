# Last updated: 6/25/2025, 4:09:38 AM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x*x + y*y  # We use squared distance
            heapq.heappush(heap, (dist, [x, y]))
    
        # Extract K smallest distance points
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result