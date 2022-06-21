# problem link -> https://leetcode.com/problems/valid-number/submissions/

class Solution:
    def isNumber(self, s: str) -> bool:

        def isinteger(temp):
            if temp == "":
                return False
            if temp[0] == '-' or temp[0] == '+':
                temp = temp[1:]

            return temp.isnumeric()

        def isdecimal(temp):
            if '.' not in temp:
                return False
            lst2 = temp.split('.')
            if len(lst2) > 2:
                return False

            if temp[0] == '.':
                return temp[1:].isnumeric()
            if temp[-1] == '.':
                return isinteger(temp[:-1])

            return (isinteger(lst2[0]) or lst2[0]=='-' or lst2[0] == '+') and lst2[1].isnumeric()
                    
        s = s.upper()

        if 'E' not in s:
            return isdecimal(s) or isinteger(s)

        lst = s.split('E')

        if len(lst) > 2:
            return False

        elif len(lst) == 1:
            return False

        return (isdecimal(lst[0]) or isinteger(lst[0])) and isinteger(lst[1])