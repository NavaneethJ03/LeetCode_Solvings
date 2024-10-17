class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(','}':'{',']':'['}
        stk = []
        for c in s:
            if c not in hashmap:
                stk.append(c)
            else:
