# problem link -> https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        if digits == '':
            return []
        
        if len(digits) == 1:
            return list(map[digits])

        possibilities = []

        values = map[digits[0]]
        for letter in values:
            for possibility in self.letterCombinations(digits[1:]):
                possibilities.append(letter + possibility)

        return possibilities