# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        count = 1
        start = None
        end = None
        while count != b + 1:
            if count == a:
                start = curr
            if count == b:
                end = curr.next.next
            curr = curr.next
            count += 1

        start.next = list2
        while start.next:
            start = start.next
        start.next = end
        return list1

        
        