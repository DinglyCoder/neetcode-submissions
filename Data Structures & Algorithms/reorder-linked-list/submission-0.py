# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        # slow is at middle

        # reverse linked list from slow point

        cur = slow.next
        slow.next = None
        prev = None
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        first = head
        second = prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
        return


        