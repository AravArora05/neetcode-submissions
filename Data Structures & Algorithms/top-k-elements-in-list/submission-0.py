class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #top K Frequent Elements
        #simple as having buckets, #and so you really just get a counter of each 
        #and put in there
        frequent = Counter(nums)
        #okay so you have the frequency of each values
        arr = [[] for i in range(len(nums) + 1)]
        for num in frequent:
            arr[frequent[num]].append(num)
            #because you want all of the nums
        j = 0
        ans = []
        for i in range(len(arr) - 1, -1, -1):
            if j == k:
                break
            if not arr[i]:
                continue
            else:
                for p in range(len(arr[i])):
                    ans.append(arr[i][p])
                    j+= 1
                    if j == k:
                        break

        return ans

            
