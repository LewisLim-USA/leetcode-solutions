# Last updated: 6/25/2025, 4:09:41 AM
class Solution:
    def search(self, arr: list[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1 
