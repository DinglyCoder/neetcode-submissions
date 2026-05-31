# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        header, prev = None, None
        p1, p2 = None, None
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val < list2.val:
            header = list1
            p1 = list1.next
            p2 = list2
        else:
            header = list2
            p1 = list1
            p2 = list2.next

        prev = header
        while (p1 != None and p2 != None):
            if (p1.val < p2.val):
                prev.next = p1
                p1 = p1.next
                prev = prev.next
            else:
                prev.next = p2
                p2 = p2.next
                prev = prev.next

        while(p1 != None):
            prev.next = p1
            p1 = p1.next
            prev = prev.next
        while(p2 != None):
            prev.next = p2
            p2 = p2.next
            prev = prev.next
        
        return header
            