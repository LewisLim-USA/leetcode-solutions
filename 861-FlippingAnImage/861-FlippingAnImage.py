# Last updated: 6/25/2025, 4:09:40 AM
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                row[i] ^= 1
        return image
