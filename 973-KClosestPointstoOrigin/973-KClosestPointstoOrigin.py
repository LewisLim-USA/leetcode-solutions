# Last updated: 5/23/2025, 12:37:51 PM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x*x + y*y  # We use squared distance
            heapq.heappush(heap, (dist, [x, y]))
    
        # Extract K smallest distance points
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result