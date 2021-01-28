# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if p and not q:
        return False
    if q and not p:
        return False
    if p.val != q.val:
        return False

    left_ans = helper(p.left, q.left)
    right_ans = helper(p.right, q.right)

    return left_ans and right_ans

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        return helper(p,q)
