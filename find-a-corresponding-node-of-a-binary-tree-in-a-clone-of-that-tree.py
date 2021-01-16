# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def getTargetCopyHelper(original, cloned, target):
    if original == None:
        return None
    if original == target:
        return cloned
    left_ans = getTargetCopyHelper(original.left, cloned.left, target)
    if left_ans != None:
        return left_ans
    right_ans = getTargetCopyHelper(original.right, cloned.right, target)
    if right_ans != None:
        return right_ans
    return None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return getTargetCopyHelper(original, cloned, target)
    
