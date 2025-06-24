# Last updated: 6/25/2025, 4:09:53 AM
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
