class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        valuesSet=set(nums)
        maxConsecutive=0
        for value in valuesSet:
            if (value - 1) in valuesSet:
                continue
            nums = value
            count = 0
            while nums in valuesSet:
                count+=1
                nums+=1
            maxConsecutive=max(maxConsecutive, count)
        return maxConsecutive

        