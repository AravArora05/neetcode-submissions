class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        allValues=set()
        for value in nums:
            if value in allValues:
                return True
            allValues.add(value)
        return False
        