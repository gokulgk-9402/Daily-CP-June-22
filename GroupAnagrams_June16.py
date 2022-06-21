# problem link -> https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key in dct:
                dct[key].append(strs[i])
            else:
                dct[key] = [strs[i]]

        ans = []
        for key in dct.keys():
            ans.append(dct[key])

        return ans