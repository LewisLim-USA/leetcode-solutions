# Last updated: 6/25/2025, 4:10:13 AM
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        # Step 1: Check missing character types
        missing_lower = 1
        missing_upper = 1
        missing_digit = 1
        for c in password:
            if c.islower(): missing_lower = 0
            elif c.isupper(): missing_upper = 0
            elif c.isdigit(): missing_digit = 0
        missing_types = missing_lower + missing_upper + missing_digit

        # Step 2: Find repeating groups
        repeats = []
        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                l = i - 2
                while i + 1 < n and password[i + 1] == password[i]:
                    i += 1
                repeats.append(i - l + 1)
            i += 1

        if n < 6:
            return max(missing_types, 6 - n)

        elif n <= 20:
            return max(missing_types, sum(r // 3 for r in repeats))

        else:
            # Step 3: Need to delete n - 20 chars
            over_len = n - 20
            replacements = 0
            # Store repeats in a min-heap based on mod 3 (to prioritize deletes)
            import heapq
            heap = []
            for r in repeats:
                heapq.heappush(heap, (r % 3, r))

            while heap and over_len > 0:
                mod, r = heapq.heappop(heap)
                if r < 3:
                    continue
                # delete one char
                r -= 1
                over_len -= 1
                heapq.heappush(heap, (r % 3, r))

            # After deletion, compute remaining replacements
            while heap:
                _, r = heapq.heappop(heap)
                if r >= 3:
                    replacements += r // 3

            return (n - 20) + max(missing_types, replacements)
