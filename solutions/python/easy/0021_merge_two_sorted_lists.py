"""
Problem ID : 0021
Title      : Merge Two Sorted Lists
Language   : Python
Solved Date: 2026-07-17
"""# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1     
                list1 = list1.next    
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        result = dummy.next
        return result
        