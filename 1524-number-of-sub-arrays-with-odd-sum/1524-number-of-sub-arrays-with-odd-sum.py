class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod = 10**9+7
        prefix_parity = 0
        even =1
        odd =0
        ans = 0
        for num in arr:
            prefix_parity = (prefix_parity +num) % 2
            if prefix_parity ==0:
                ans += odd
                even+=1
            else:
                ans+= even
                odd+=1
        return ans%mod