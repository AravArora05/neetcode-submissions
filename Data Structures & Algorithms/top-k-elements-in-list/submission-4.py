class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #find the k most frequent elements w/ in the array
        #so the brute force way is the heap solution
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for val in nums:
            count[val]+=1
        for key, val in count.items():
            freq[val].append(key)
        z = 0
        res = []
        for i in range(len(freq) - 1, 0, -1):
            if not freq[i]:
                continue
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res


            
        