class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a,b = len(word1),len(word2)
        A ,B = 0 , 0
        step = 1
        s = []

        while A<a and B<b :
            if step == 1:
                s.append(word1[A])
                A+=1
                step = 2
            else:
                s.append(word2[B])
                B+=1
                step = 1
        while A < a :
            s.append(word1[A])
            A+=1  
        while B < b :
            s.append(word2[B])
            B+= 1 

        return ''.join(s)
