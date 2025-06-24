# Last updated: 6/25/2025, 4:09:46 AM
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        def flatten_dfs(prev, curr):
            if not curr:
                return prev

            curr.prev = prev
            prev.next = curr

            # Save next pointer
            temp_next = curr.next

            # Recursively flatten the child list
            tail = flatten_dfs(curr, curr.child)
            curr.child = None

            # Continue with the next node
            return flatten_dfs(tail, temp_next)

        # Create a dummy node to simplify prev connections
        dummy = Node(0, None, head, None)
        flatten_dfs(dummy, head)
        dummy.next.prev = None  # Remove dummy
        return dummy.next
