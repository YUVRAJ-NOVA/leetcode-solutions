class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', '[':']', '{': '}'}
        i = 0
        while i < len(s) - 1:
            if s[i] in pairs and s[i+1] == pairs[s[i]]:
                s = s[:i] + s[i+2:]    
                i = max(i - 1, 0)       
            else:
                i += 1
        return len(s) == 0              