# Last updated: 6/25/2025, 4:10:12 AM
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Build Trie
        trie = {}
        for num in nums:
            node = trie
            for i in reversed(range(32)):  # 31 to 0
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
        
        max_xor = 0
        for num in nums:
            node = trie
            xor = 0
            for i in reversed(range(32)):
                bit = (num >> i) & 1
                # Try to take the opposite bit to maximize XOR
                toggle = 1 - bit
                if toggle in node:
                    xor = (xor << 1) | 1
                    node = node[toggle]
                else:
                    xor = (xor << 1)
                    node = node[bit]
            max_xor = max(max_xor, xor)
        
        return max_xor

        