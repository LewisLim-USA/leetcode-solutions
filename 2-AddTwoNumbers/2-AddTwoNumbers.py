# Last updated: 5/12/2025, 12:28:04 PM

from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = result = ListNode(None)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry % 10)
            prev = prev.next
            carry //= 10
        return result.next
