class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for ops in operations:
            if ops == "+":
                stk.append(int(stk[-1]) + int(stk[-2]))
            elif ops == "D":
                stk.append(2*int(stk[-1]))
            elif ops == "C":
                stk.pop()
            else:
                stk.append(int(ops))
            return sum(stk)


# Time Complexity - O(n)
