# Last updated: 5/17/2025, 11:17:39 PM
class Solution:
    def search(self, arr: list[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        # <= because left and right could point to the same element, < would miss it
        while left <= right:
            # double slash for integer division in python 3,
            # we don't have to worry about integer `left + right` overflow
            # since python integers can be arbitrarily large
            mid = (left + right) // 2
            # found target, return its index
            if arr[mid] == target:
                return mid
            # middle less than target, discard left half by making left search boundary `mid + 1`
            if arr[mid] < target:
                left = mid + 1
            # middle greater than target, discard right half by making right search boundary `mid - 1`
            else:
                right = mid - 1
        return -1  # if we get here we didn't hit above return so we didn't find target
