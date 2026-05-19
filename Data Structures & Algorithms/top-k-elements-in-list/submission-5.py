class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        freq=[[] for i in range(len(nums) + 1)]

        for num, count in count.items():
            freq[count].append(num)
        ans=[]
        for i in range(len(freq) - 1, -1, -1):
            for val in freq[i]:
                ans.append(val)
                if len(ans) ==k:
                    return ans
        

        
        