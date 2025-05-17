# Last updated: 5/17/2025, 11:24:48 PM
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
