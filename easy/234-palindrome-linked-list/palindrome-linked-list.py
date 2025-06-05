# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or  not head.next:
            return True

        # Get Mid point of list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # reverse the second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
       
        # check palindrome
        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
            
            



        