class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = len(nums1)
        y = len(nums2)
        if x > y:
            x,y = y,x
            nums1, nums2 = nums2, nums1
        # ensured x is the smaller array

        low = 0
        high = x

        while low <= high:
            partition_x = (low+high)//2
            partition_y = (x+y+1)//2 - partition_x

            max_left_x = -2**31 if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = 2**31 - 1 if partition_x == x else nums1[partition_x]

            max_left_y = -2**31 if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = 2**31 - 1 if partition_y == y else nums2[partition_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x + y)%2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y))/2
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                high = partition_x - 1
            elif max_left_y > min_right_x:
                low = partition_x + 1
            else:
                print('wtf')
