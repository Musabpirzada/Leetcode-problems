#Approach 1 with more memory usage

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node == None:
            pass
        else:
            next_node = node.next
            node.val = next_node.val
            node.next = next_node.next
            
            

#Approach 2nd with less Memory usage
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next
