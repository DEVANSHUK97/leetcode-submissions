# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def rangeSumBST_helper(root: TreeNode, low: int, high: int) -> int:
    if root == None:
        return 0
    if root.val >= low and root.val <= high:
        return root.val + rangeSumBST_helper(root.left, low, high) + rangeSumBST_helper(root.right, low, high)
    elif root.val < low:
        return rangeSumBST_helper(root.right, low, high)
    elif root.val > high:
        return rangeSumBST_helper(root.left, low, high)
    else:
        print("this will never execute")

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return rangeSumBST_helper(root, low, high)
