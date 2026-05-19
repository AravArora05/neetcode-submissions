class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        #finds the frequecny of each value in the nums array
        #hashamp - O(n) time
        count = [[] for i in range(len(nums) + 1)]
        for key, val in freq.items():
            count[val].append(key)
        
        res=[]
        for i in range(len(count) -1, -1, -1):
            for num in count[i]:
                res.append(num)
                if len(res)==k:
                    return res
                

        
        
        