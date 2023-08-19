# -*- coding: utf-8 -*-
"""merged_two_sorted_list.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x9HzKvYzUCRLYoRNITwgXjVKgC1d4The
"""

#With High Memory Useage

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 != None and list2 == None:
            return list1
        elif list2 != None and list1 == None:
            return list2
        else:
            dummy = ListNode(0)
            p = dummy
            while list1 != None and list2 != None:
                if list1.val < list2.val:
                    p.next = list1
                    list1 = list1.next
                else:
                    p.next = list2
                    list2 = list2.next
                p = p.next
            if list1 != None:
                p.next = list1
            if list2 != None:
                p.next = list2
            return dummy.next

# With Low Memory Useage


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        p = dummy

        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next

        p.next = list1 or list2

        return dummy.next