class Solution:
    def fxn(self, nums, dp,n):
        n = len(nums)
        dp[0]=nums[0]
        for i in range(1,n):
            if i>1:
                pick = nums[i] + dp[i-2]
            else:
                pick = nums[i]
            not_pick = 0+dp[i-1]
            dp[i] = max(pick, not_pick)
        return dp[n-1]


    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp=[-1]*n
        return self.fxn(nums, dp,n)
