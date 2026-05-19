class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #given two integeres
        #return the indicies such that nums[i] + nums[j] == target
        hashmap={}
        for i, value in enumerate(nums):
            if (target - value) in hashmap:
                return [hashmap[target - value], i]
            hashmap[value]=i
        

        
        