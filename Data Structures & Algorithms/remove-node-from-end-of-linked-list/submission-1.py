# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1

        cur = head
        index = 0
        removeIndex = length - n
        if removeIndex == 0:
                return head.next

        while cur:
            if index == removeIndex - 1:
                if cur.next:
                    cur.next = cur.next.next
                else:
                    cur.next = None
                break
            cur = cur.next
            index += 1


        return head
