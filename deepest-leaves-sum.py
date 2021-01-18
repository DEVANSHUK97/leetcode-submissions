# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def max_depth(root):
    if root.left == None and root.right == None:
        return 1
    left_max = 0
    right_max = 0
    if root.left != None:
        left_max = max_depth(root.left)
    if root.right != None:
        right_max = max_depth(root.right)
    return 1 + max(left_max, right_max)

def helper(root, height, mx):
    if root == None:
        return 0
    if height == mx:
        return root.val
    l_sum = 0
    r_sum = 0
    if root.left != None:
        l_sum = helper(root.left, height + 1, mx)
    if root.right != None:
        r_sum = helper(root.right, height + 1, mx)
    return l_sum + r_sum

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        mx = max_depth(root)
        print(mx)
        return helper(root,1, mx)
