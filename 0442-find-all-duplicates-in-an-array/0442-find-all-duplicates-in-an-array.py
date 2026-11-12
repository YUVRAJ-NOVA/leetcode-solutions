from collections import Counter
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        record = Counter(nums)
        return [x for x, c in record.items() if c>1]