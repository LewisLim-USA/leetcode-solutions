# Last updated: 5/12/2025, 9:33:16 AM
class Solution:
    def findTarget(self, root, k):
        hashmap = set()
        
        def dfs(node):
            if not node:
                return False
            complement = k - node.val
            if complement in hashmap:
                return True
            hashmap.add(node.val)
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
