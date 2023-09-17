# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        part_size = length // k
        extra_parts = length % k


        result = []


        current = head
        for i in range(k):
            part_head = current

            part_length = part_size + (1 if extra_parts > 0 else 0)
            extra_parts -= 1

            for j in range(part_length - 1):
                if current:
                    current = current.next

            if current:
                next_node = current.next
                current.next = None
                current = next_node

            result.append(part_head)

        return result
