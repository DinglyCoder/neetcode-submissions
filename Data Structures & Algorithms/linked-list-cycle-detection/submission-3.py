# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == None:
            return False

        p1 = head
        p2 = head.next

        while (p1 != None and p2 != None and p2.next != None and p1 != p2):
            p1 = p1.next
            p2 = p2.next.next

        if p1 == None or p2 == None or p2.next == None:
            return False
        return p1 == p2
        