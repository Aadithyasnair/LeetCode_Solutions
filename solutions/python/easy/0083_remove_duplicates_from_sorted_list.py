"""
Problem ID : 0083
Title      : Remove Duplicates from Sorted List
Language   : Python
Solved Date: 2026-07-17
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        if current==None:
            return head
        else:
            while current.next and current:
                if current.val==current.next.val:
                    current.next=current.next.next
                else:
                    current=current.next
        return head