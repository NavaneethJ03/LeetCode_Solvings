class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0 
        n = len(s)
        m = len(t)
        if s == '': return True
        if n > m : return False
        
        for i in range(m):
            if t[i] == s[j]:
                
                if j == n - 1:
