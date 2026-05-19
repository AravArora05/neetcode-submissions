class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqVals = set(nums)
        #you have a set of nums
        if not nums:
            return 0
        longest=1
        for value in uniqVals:
            if (value - 1) in uniqVals:
                continue
            currLength=1
            while (value + 1) in uniqVals:
                currLength+=1
                value+=1
            longest=max(currLength, longest)
        return longest
        