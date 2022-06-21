# problem link -> https://leetcode.com/problems/substring-with-concatenation-of-all-words/

import string
from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        string_length = len(s)
        no_of_words = len(words)
        word_length = len(words[0])

        concatenation_size = word_length * no_of_words

        word_count = Counter(words)

        def check(i):
            remaining = word_count.copy()
            words_used = 0
            for j in range(i, i + concatenation_size, word_length):
                substring = s[j:j+word_length]

                if remaining[substring] > 0:
                    remaining[substring] -= 1
                    words_used += 1

                else:
                    break
                
            return words_used == no_of_words

        ans = []
        for i in range(string_length -concatenation_size + 1):
            if check(i):
                ans.append(i)

        return ans


