# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        elif head != None and head.next == None:
            return head
        else:
            lookup = {}
            current = head
            prev = head
            while current != None:
                if current.val in lookup:
                    prev.next = prev.next.next
                else:
                    lookup[current.val] = True
                    prev = current
                current = current.next
            return head

#With Much Less memory useage.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


#WIth BETTER RUNTIME

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if current is None:
            return None

        # Create a dummy node to mark the beginning of the list without duplicates.
        sentinel = ListNode(0, current)
        previous = sentinel

        while current is not None:
            if current.next is not None and current.val == current.next.val:
                # Skip all consecutive duplicate nodes.
                while current.next is not None and current.val == current.next.val:
                    current = current.next
            else:
                # The current node is not a duplicate, so move it to the next node without duplicates.
                previous.next = current
                current = current.next
                previous = previous.next

        return sentinel.next
