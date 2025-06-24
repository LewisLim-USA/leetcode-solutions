# Last updated: 6/25/2025, 4:12:04 AM
from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # Build the initial heap
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))
        
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next
