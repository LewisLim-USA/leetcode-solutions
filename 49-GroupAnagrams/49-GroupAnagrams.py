# Last updated: 6/25/2025, 4:11:20 AM
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # Sort the word to create a common key for anagrams
            key = tuple(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())
