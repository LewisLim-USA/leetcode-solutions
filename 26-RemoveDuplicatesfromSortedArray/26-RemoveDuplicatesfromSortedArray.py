# Last updated: 6/25/2025, 4:01:42 AM
import collections
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        n = len(words)
        i = 0

        while i < n:
            current_line_words = []
            current_line_length = 0
            j = i

            # Step 1: Greedy pack words into the current line
            # We add 1 for the space that would follow each word (except the last one in the line)
            while j < n and current_line_length + len(words[j]) + (1 if current_line_words else 0) <= maxWidth:
                current_line_length += len(words[j]) + (1 if current_line_words else 0) # Add space for words after the first
                current_line_words.append(words[j])
                j += 1

            # Adjust current_line_length to be the exact length of words without spaces
            current_line_length = sum(len(word) for word in current_line_words)

            num_words_on_line = len(current_line_words)

            # Step 2: Determine spaces
            line_str = ""

            # Case 1: Last line or a line with only one word
            if j == n or num_words_on_line == 1:
                line_str = " ".join(current_line_words)
                line_str += " " * (maxWidth - len(line_str))
            # Case 2: Regular line with multiple words
            else:
                total_spaces_to_add = maxWidth - current_line_length
                num_gaps = num_words_on_line - 1

                # Calculate base spaces and extra spaces to distribute
                base_spaces_per_gap = total_spaces_to_add // num_gaps
                extra_spaces = total_spaces_to_add % num_gaps

                for k in range(num_words_on_line):
                    line_str += current_line_words[k]
                    if k < num_gaps: # If it's not the last word
                        spaces_to_add = base_spaces_per_gap
                        if extra_spaces > 0:
                            spaces_to_add += 1
                            extra_spaces -= 1
                        line_str += " " * spaces_to_add

            result.append(line_str)
            i = j # Move to the next word for the next line

        return result