class Solution:
    def climbStairs(self, n: int) -> int:
        count=0
        if n==1:
            return 1
        if n==2:
            return 2
        curr=2
        prev=1
        for i in range(2, n):
            temp=curr
            curr=prev+curr
            prev=temp
        return curr
        
