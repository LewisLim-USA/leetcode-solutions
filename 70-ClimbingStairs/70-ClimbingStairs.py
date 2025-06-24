# Last updated: 6/25/2025, 4:13:19 AM
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')

        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)
