# problem link -> https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        for i in range(len(candidates)):

            if candidates[i] == target:
                ans.append([candidates[i]])

            elif candidates[i] < target:
                res = self.combinationSum(candidates[i:], target - candidates[i])
                ans += [[candidates[i]] + x for x in res]

        return ans