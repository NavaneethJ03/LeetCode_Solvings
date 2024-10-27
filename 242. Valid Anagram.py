from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f = Counter(s)
        g = Counter(t)
        if f == g:
            return True
        return False


