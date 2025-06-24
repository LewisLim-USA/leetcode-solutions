# Last updated: 6/25/2025, 4:12:00 AM
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a portion of the linked list
        def reverseLinkedList(head, k):
            new_head = None
            ptr = head
            while k:
                next_node = ptr.next
                ptr.next = new_head
                new_head = ptr
                ptr = next_node
                k -= 1
            return new_head
        
        # Check if there are at least k nodes left in the linked list
        count = 0
        ptr = head
        while count < k and ptr:
            ptr = ptr.next
            count += 1
        
        # If we have k nodes, then we reverse them
        if count == k:
            reversed_head = reverseLinkedList(head, k)
            # After reversing, the original head becomes the tail
            # and we recursively call reverseKGroup on the next part
            head.next = self.reverseKGroup(ptr, k)
            return reversed_head
        return head
