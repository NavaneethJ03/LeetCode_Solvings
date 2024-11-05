class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            if i < 2:
                result.append(s[i])
            else:
                if not (result[-1] == result[-2] == s[i]):
                    result.append(s[i])
        return ''.join(result)
        
