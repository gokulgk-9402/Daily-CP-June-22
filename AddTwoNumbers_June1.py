# problem link -> https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        p1 = l1
        p2 = l2
        prev = ListNode()
        head = ListNode()
        head = prev
        while p1 or p2 or (sum!=0):
            if p1:
                sum = sum + p1.val
                p1 = p1.next
            if p2:
                sum = sum + p2.val
                p2 = p2.next
            prev.next = ListNode(sum%10)
            sum = sum//10
            prev = prev.next
            
        return head.next
            