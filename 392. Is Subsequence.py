class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0 
        n = len(s)
        m = len(t)
        if s == '':return True
