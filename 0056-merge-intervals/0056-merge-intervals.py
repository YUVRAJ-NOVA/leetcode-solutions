class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        self.iv = sorted(intervals, key = lambda x : x[0])
        # [[1,3], [2,6], [8,10], [15,18]]
        n = len(self.iv)
        result = []
        prev = float('-inf')
        for start, end in self.iv:
            if result and start<=result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        return result