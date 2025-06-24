# Last updated: 6/25/2025, 4:11:53 AM
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_map = {}
        
        for word in words:
            word_map[word] = word_map.get(word, 0) + 1
        
        result = []
        
        for i in range(len(s) - total_len + 1):
            seen = {}
            for j in range(0, total_len, word_len):
                word = s[i+j:i+j+word_len]
                if word in word_map:
                    seen[word] = seen.get(word, 0) + 1
                    if seen[word] > word_map[word]:
                        break
                else:
                    break
            if seen == word_map:
                result.append(i)
        
        return result
