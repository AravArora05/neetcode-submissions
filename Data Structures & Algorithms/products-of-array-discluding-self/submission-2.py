class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev=1
        preFix=[1]*len(nums)
        for i in range(len(nums)):
            preFix[i]=prev
            prev*=nums[i]
        postFix=1
        for i in range(len(nums) -1, -1, -1):
            preFix[i]*=postFix
            postFix*=nums[i]
        return preFix
        