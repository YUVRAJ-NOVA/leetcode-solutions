from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for strr in strs:
            groups[''.join(sorted(strr))].append(strr)
        return list(groups.values())