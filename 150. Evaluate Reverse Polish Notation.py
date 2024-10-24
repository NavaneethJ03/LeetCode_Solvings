class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashset = {"+","-","*","/"}
        stk = []
        for i in tokens:
            if i not in hashset:
                stk.append(int(i))
            else:
                s1 =  stk.pop()
                s2 =  stk.pop()
                if i == "+":
                    stk.append(s1 + s2)
                elif i == "-":
                    stk.append(s2 - s1)
                elif i == "*":
                    stk.append(s2*s1)
