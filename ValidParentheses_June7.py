# problem link -> https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        no_normal_open = 0
        no_square_open = 0
        no_curly_open = 0
        
        last_open = []
        
        i = 0
        while i < len(s):
            if s[i] == '(':
                no_normal_open += 1
                last_open.append('(')
            elif s[i] == '[':
                no_square_open += 1
                last_open.append('[')
            elif s[i] == '{':
                no_curly_open += 1
                last_open.append('{')
            elif s[i] == ')':
                if no_normal_open == 0 or last_open[-1] != '(':
                    return False
                no_normal_open -= 1
                last_open = last_open[:-1]
            elif s[i] == ']':
                if no_square_open == 0 or last_open[-1] != '[':
                    return False
                no_square_open -= 1
                last_open = last_open[:-1]
            elif s[i] == '}':
                if no_curly_open == 0 or last_open[-1] != '{':
                    return False
                no_curly_open -= 1
                last_open = last_open[:-1]

            i+=1
                
        if no_normal_open or no_square_open or no_curly_open:
            return False
        
        return True