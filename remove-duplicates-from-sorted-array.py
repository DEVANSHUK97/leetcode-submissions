class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        first = nums[0]
        i = 1
        n = len(nums)
        while True:
            if nums[i] == first:
                nums.pop(i)
            else:
                first = nums[i]
                i = i + 1
            if i == len(nums):
                break
        return len(nums)
