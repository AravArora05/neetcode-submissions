class Solution:
    def climbStairs(self, n: int) -> int:
        #reccurence, how many ways to climb to the top of the stair case
        #to get to point n:
        stairs=[0]*(n+1)
        nums=stairs
        if n == 2:
            return 2
        if n==1:
            return 1
        nums[0]=0
        nums[1]=1
        nums[2]=2
        for i in range(3, len(stairs)):
            nums[i]=nums[i -1] + nums[i - 2]
        return stairs[n]
            

        