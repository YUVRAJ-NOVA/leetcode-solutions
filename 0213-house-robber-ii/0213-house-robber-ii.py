class Solution:
    def fxn(self, nums, n):
        n = len(nums)
        prev = nums[0]
        prev2=0
        curr =nums[0]
        for i in range(1,n):
            if i>1:
                pick = nums[i] + prev2
            else:
                pick = nums[i]
            not_pick = 0+prev
            curr = max(pick, not_pick)
            prev2=prev
            prev = curr
        return prev


    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n = len(nums)
        ans1= self.fxn(nums[0:n-1], n-1)
        ans2= self.fxn(nums[1:n], n-1)
        return max(ans1, ans2)
