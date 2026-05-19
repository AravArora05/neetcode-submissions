class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        allVal=set()
        for n in nums:
            if n in allVal:
                return True
            allVal.add(n)
        return False
        