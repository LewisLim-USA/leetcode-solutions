# Last updated: 6/25/2025, 4:10:07 AM
class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.key_count = {}       # key -> count
        self.count_node = {}      # count -> node
        self.head = Node(float('-inf'))  # Dummy head
        self.tail = Node(float('inf'))   # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node, prev_node):
        nxt = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = nxt
        nxt.prev = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_node[node.count]

    def inc(self, key: str) -> None:
        count = self.key_count.get(key, 0)
        new_count = count + 1
        self.key_count[key] = new_count

        if new_count not in self.count_node:
            new_node = Node(new_count)
            self.count_node[new_count] = new_node
            prev_node = self.count_node[count] if count in self.count_node else self.head
            self._add_node_after(new_node, prev_node)

        self.count_node[new_count].keys.add(key)

        if count > 0:
            self.count_node[count].keys.remove(key)
            if not self.count_node[count].keys:
                self._remove_node(self.count_node[count])

    def dec(self, key: str) -> None:
        count = self.key_count[key]
        new_count = count - 1
        self.count_node[count].keys.remove(key)

        if new_count == 0:
            del self.key_count[key]
        else:
            self.key_count[key] = new_count
            if new_count not in self.count_node:
                new_node = Node(new_count)
                self.count_node[new_count] = new_node
                self._add_node_after(new_node, self.count_node[count].prev)
            self.count_node[new_count].keys.add(key)

        if not self.count_node[count].keys:
            self._remove_node(self.count_node[count])

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
