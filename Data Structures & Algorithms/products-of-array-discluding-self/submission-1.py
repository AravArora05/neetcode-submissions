class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrayFirst=1
        ans=[1] * len(nums)
        for i in range(len(nums)):
            ans[i]*=arrayFirst
            arrayFirst*=nums[i]
        post=1
        for i in range(len(nums) - 1, -1, -1):
            ans[i]*=post
            post*=nums[i]
        return ans
        