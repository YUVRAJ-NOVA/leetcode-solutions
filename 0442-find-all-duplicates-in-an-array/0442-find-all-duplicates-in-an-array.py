from collections import Counter
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        return [x for x,c in Counter(nums).items() if c>1]