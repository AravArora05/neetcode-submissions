class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1
        nums=numbers
        while l < r:
            summ=nums[l] + nums[r]
            if summ > target:
                r-=1
            elif summ < target:
                l+=1
            else:
                return [l +1, r + 1]

        