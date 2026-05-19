class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = set()
        for value in nums:
            if value in arr:
                return True
            arr.add(value)
        return False
        