class MedianFinder:
    def __init__(self):
        self.nums = []
        self.total = 0

    def addNum(self, num: int) -> None:
        insort(self.nums, num)
        self.total += 1

    def findMedian(self) -> float:
        if self.total % 2:
            return self.nums[self.total//2]

        return (self.nums[self.total//2] + self.nums[self.total//2 - 1])/2
