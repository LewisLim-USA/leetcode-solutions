# Last updated: 6/25/2025, 4:11:03 AM
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Count the length
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Make the list circular
        tail.next = head

        # Step 3: Find new tail: (length - k % length - 1)th node
        #         and new head: (length - k % length)th node
        k = k % length
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next

        # Step 4: Break the circle
        new_tail.next = None

        return new_head
