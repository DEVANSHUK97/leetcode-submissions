# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = 0
        h = head
        while h:
            n = n + 1
            h = h.next
        multiplier = 2**(n-1)
        ans = 0
        h = head
        while h:
            ans = ans + multiplier*h.val
            multiplier = multiplier / 2
            h = h.next
        return int(ans)
