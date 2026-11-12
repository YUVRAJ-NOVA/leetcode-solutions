class Solution:
    def canJump(self, nums: list[int]) -> bool:
        far = 0
        for i, step in enumerate(nums):
            if i>far:
                return False
            far = max(far, i+step)
        return True
