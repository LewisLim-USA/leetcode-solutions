# Last updated: 6/25/2025, 4:10:38 AM
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        # Step 1: Use a set for O(1) lookups
        wordSet = set(wordList)
        if endWord not in wordSet:
            # If the end word is not in the dictionary, no solution
            return 0

        from collections import deque
        
        # Step 2: Use a queue for BFS
        queue = deque()
        queue.append((beginWord, 1))  # (current word, steps taken so far)

        while queue:
            currentWord, steps = queue.popleft()

            # Step 3: Check if we've reached the endWord
            if currentWord == endWord:
                return steps

            # Step 4: Try changing each letter in currentWord
            for i in range(len(currentWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    # Change one letter at position i
                    newWord = currentWord[:i] + c + currentWord[i+1:]

                    # If the new word is in the set, it's a valid next step
                    if newWord in wordSet:
                        wordSet.remove(newWord)  # avoid revisiting
                        queue.append((newWord, steps + 1))

        # If queue is empty and endWord was never reached
        return 0
