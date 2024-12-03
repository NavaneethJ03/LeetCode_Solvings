class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L = 1 
        R = num 
        
        while L <= R :
            M =  L +((R-L)//2)
            m_sq = M * M
            if num ==  m_sq:
                return True
            elif num > m_sq:
                L = M + 1
            else:
                R =  M - 1 
        return False
# Time Complexity -  O(log n )
# Space Complexity -  O(1)
        
