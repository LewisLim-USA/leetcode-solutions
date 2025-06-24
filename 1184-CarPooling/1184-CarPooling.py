# Last updated: 6/25/2025, 4:09:31 AM
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Imagine this as a church van traveling across locations 0 to 1000
        # Each index in `timeline` represents a location or time checkpoint
        timeline = [0] * 1001

        for num_passengers, start, end in trips:
            # At the pickup point, passengers get into the van
            timeline[start] += num_passengers
            # At the drop-off point, passengers leave the van
            timeline[end] -= num_passengers

        # This keeps track of how many people are in the van as it moves
        passengers = 0
        for change in timeline:
            passengers += change
            # If the van ever exceeds capacity, trip isn't possible
            if passengers > capacity:
                return False

        # All trips completed safely within van capacity
        return True
