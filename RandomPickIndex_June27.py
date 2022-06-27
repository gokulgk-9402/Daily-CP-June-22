# problem link -> https://leetcode.com/problems/random-pick-index/

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.mem = {}

    def pick(self, target: int) -> int:
        if target in self.mem.keys():
            return random.choice(self.mem[target])
        indices = []
        for index in range(len(self.nums)):
            if self.nums[index] == target:
                indices.append(index)
        self.mem[target] = indices
        return random.choice(indices)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)