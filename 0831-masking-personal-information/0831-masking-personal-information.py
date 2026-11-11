class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            at = s.index('@')
            return s[0]+'*****'+s[at-1:]
        digits = [ch for ch in s if ch.isdigit()]
        local = '***-***-' + ''.join(digits[-4:])
        extra = len(digits)-10
        if extra == 0:
            return local
        return '+' + '*'*extra + '-' +local

        