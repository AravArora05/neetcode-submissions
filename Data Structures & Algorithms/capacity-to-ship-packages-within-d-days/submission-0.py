class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #convey belt must # be shipped within days days
        #ith package on the conveyer
        l=max(weights)
        r=sum(weights)
        ans=sum(weights)
        print(r)
        while l<=r:
            mid=(l+r)//2
            curr_day=0
            count=1
            for day in weights:
                if (curr_day+day)>mid:
                    curr_day=day
                    count+=1
                else:
                    curr_day+=day
            if count<=days:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
                
                


        