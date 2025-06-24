# Last updated: 6/25/2025, 4:11:37 AM
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()  # Sort to easily skip duplicates
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return result
