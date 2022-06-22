# problem link -> https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        ans = []

        if len(words) == 0:
            return ans

        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

        for word in words:
            tmp = word.lower()
            if tmp[0] in keyboard[0]:
                row = 0

            elif tmp[0] in keyboard[1]:
                row = 1

            else:
                row = 2

            flag = 1

            for ch in tmp[1:]:
                if ch not in keyboard[row]:
                    flag = 0

            if flag:
                ans.append(word)

        return ans