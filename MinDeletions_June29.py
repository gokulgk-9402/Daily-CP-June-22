# problem link -> https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = Counter(s)
        freq_list = list(frequencies.values())
        max_freq = max(freq_list)
        freq_counter = Counter(freq_list)

        result = 0
        for i in range(max_freq):
            if freq_counter.get(i) is None:
                freq_counter[i] = 0

        for i in range(max_freq, 0, -1):
            if freq_counter[i] > 1:
                freq_counter[i-1] += freq_counter[i] - 1
                result += freq_counter[i] - 1
                freq_counter[i] = 1

        return result