# problem link -> https://leetcode.com/problems/merge-two-sorted-lists/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        h1, h2 = list1, list2
        ans = ListNode()
        anshead = ans
        while h1!= None or h2!= None:
            if h1 == None:
                ans.next = ListNode(h2.val, None)
                h2 = h2.next
            elif h2 == None:
                ans.next = ListNode(h1.val, None)
                h1 = h1.next
            elif h1.val < h2.val:
                ans.next = ListNode(h1.val, None)
                h1 = h1.next
            else:
                ans.next = ListNode(h2.val, None)
                h2 = h2.next

            ans = ans.next

        return anshead.next