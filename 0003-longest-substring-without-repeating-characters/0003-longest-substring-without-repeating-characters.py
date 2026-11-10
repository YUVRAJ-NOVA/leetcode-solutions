class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        if len(s)==0:
            return 0
        seen = set()
        ans = 0
        left =0
        for right, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[left])
                left+=1    
            seen.add(ch)
            count = right - left+1
            ans = max(ans, count)
        return ans