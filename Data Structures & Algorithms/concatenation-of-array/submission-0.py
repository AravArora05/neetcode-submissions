class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_arr=[0]*(len(nums)*2)
        for i in range(len(new_arr)):
            new_arr[i]=nums[i%len(nums)]
        return new_arr

        