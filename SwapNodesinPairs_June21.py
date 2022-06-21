# problem link -> https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
        
        nh = head.next.next
        temp = head
        head = head.next
        temp.next = self.swapPairs(nh)
        head.next = temp
        
        return head