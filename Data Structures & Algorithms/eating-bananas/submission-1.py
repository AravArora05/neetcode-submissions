class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=r
        while l<=r:
            mid=(l+r)//2
            hours=0
            for bananas in piles:
                #because if mid is like 5 and you have 7 it takes days
                hours+=math.ceil(bananas/mid)
            if hours<=h:
                #that means youre eating too many bananas
                r=mid-1
                ans=mid
            else:
                l=mid+1
        return ans
            
                #try less banans
        #bc the max you can in a day is soley the number 