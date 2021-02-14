class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(\
                   list(\
                        map(\
                            lambda x: \
                            0 if len(str(x))&1 else 1,\
                            nums
                           )
                       )
                  )
