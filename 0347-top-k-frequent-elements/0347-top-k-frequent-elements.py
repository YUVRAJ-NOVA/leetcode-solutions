from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        record = Counter(nums)
        return [key for key, value in record.most_common(k)]
        