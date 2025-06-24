# Last updated: 6/25/2025, 4:12:02 AM
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if there are fewer than two nodes left
        if not head or not head.next:
            return head
        
        # Nodes to swap
        first_node = head
        second_node = head.next
        
        # Swap
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        
        return second_node
