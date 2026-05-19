class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #top k frequence elemnt, and ave it sorted correctly in the array
        vals = Counter(nums)
        #you have a counter of all the values
        arr = [[] for i in range(len(nums) + 1)]
        #looking through each value in values
        for v in vals:
            arr[vals[v]].append(v)
        #so you're appending it to tehr ight place
        d = 0
        ans = []
        for i in range(len(arr) -1, -1, -1):
            if not arr[i]:
                continue
            for j in range(len(arr[i])):
                ans.append(arr[i][j])
                d += 1
                if d == k:
                    return ans
        return ans


        