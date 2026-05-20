class Solution:
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #given a sorted integeray array, arr
        #k, x
        #find where |a-x| < |b-x|
        #and where |a-x| ==b-x
        l=0
        i=0
        r=k
        bestl=0
        bestr=k
        max_curr=float("inf")
        curr_range=0
        while i<r:
            curr_range+=abs(x-arr[i])
            i+=1   
        max_curr=curr_range

        while r < len(arr):
            #so you will keep adding and shifiting
            curr_range-=abs(x-arr[l])
            l+=1
            curr_range+=abs(x-arr[r])
            
            if curr_range<max_curr:
                max_curr=curr_range
                bestl=l
                bestr=r+1
            r+=1
            
        return arr[bestl: bestr]
            #r will be done automatically
            
        