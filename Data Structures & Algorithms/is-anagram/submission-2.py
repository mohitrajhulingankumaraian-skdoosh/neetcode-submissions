from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_hash = Counter(s)
        t_hash = Counter(t)
        return True if s_hash == t_hash else False
        