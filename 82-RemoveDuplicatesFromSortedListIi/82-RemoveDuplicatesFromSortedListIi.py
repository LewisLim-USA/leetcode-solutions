# Last updated: 6/25/2025, 4:10:43 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            # Check for duplicates
            if current.next and current.val == current.next.val:
                # Skip all nodes with the same value
                while current.next and current.val == current.next.val:
                    current = current.next
                # Link prev to the node after the last duplicate
                prev.next = current.next
            else:
                # No duplicates; move prev pointer
                prev = prev.next
            current = current.next

        return dummy.next
