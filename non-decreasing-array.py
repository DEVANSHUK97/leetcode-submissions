class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        how_many = 0
        where = 0
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                how_many = how_many + 1
                where = i
        if how_many == 0:
            return True
        if how_many > 1:
            return False
        else:
            print(where, nums[where])
            if where == 1 or where == n-1:
                return True
            else:
                if nums[where - 1] <= nums[where + 1]:
                    return True
                else:
                    if nums[where - 2] <= nums[where]:
                        return True
                    else:
                        return False
        
