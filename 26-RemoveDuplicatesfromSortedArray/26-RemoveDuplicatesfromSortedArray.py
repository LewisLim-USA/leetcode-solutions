# Last updated: 6/25/2025, 4:09:05 AM
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            raise ValueError("Input must be a non-negative integer")
        if x == 0:
            return 0
        if x == 1:
            return 1

        left = 0
        right = x
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            
            # Avoid potential overflow if mid*mid is very large
            # This check is often not strictly necessary in Python due to arbitrary precision integers,
            # but it's good practice for languages with fixed-size integers (e.g., Java, C++)
            # if mid > x // mid and mid != 0: # This check can be used to prevent overflow
            #     right = mid - 1
            #     continue

            mid_squared = mid * mid

            if mid_squared == x:
                return mid
            elif mid_squared < x:
                ans = mid  # mid could be the answer, or we can find a larger one
                left = mid + 1
            else:  # mid_squared > x
                right = mid - 1
        
        return ans