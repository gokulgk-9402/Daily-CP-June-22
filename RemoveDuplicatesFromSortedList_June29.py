# problem link -> https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp = head
        # last_val = head.val
        while temp != None:
            temp2 = temp.next
            while temp2!=None and temp2.val == temp.val:
                temp2 = temp2.next
            temp.next = temp2
            temp = temp.next
            
        return head
        