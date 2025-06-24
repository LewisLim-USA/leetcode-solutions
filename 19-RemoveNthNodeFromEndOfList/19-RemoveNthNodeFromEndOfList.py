# Last updated: 6/25/2025, 4:12:10 AM
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the nth node
        slow.next = slow.next.next
        
        return dummy.next
