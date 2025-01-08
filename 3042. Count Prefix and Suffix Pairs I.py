class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0 
        for i in range(n):
            s1 = words[i]
            for j in range(i + 1 , n):
                s2 = words[j]

                if len(s2) < len(s1):
                    pass
                else:
                    suffix =  s2[-len(s1):]
                    prefix =  s2[:len(s1)]
                
                    if prefix == s1 and suffix == s1:
                        count += 1 
        
        return count

