class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        numbers = sorted(set(nums))
        best = 1
        curr = 1
        for i in range(1, len(numbers)):
            if numbers[i] == numbers[i-1]+1:
                curr +=1
            else:
                curr = 1
            best= max(best, curr)
        return best