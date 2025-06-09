# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                # if fast is None or slow is None or fast.next is None:
                    # return false
                slow = slow.next
                fast = fast.next.next
            return True
        except AttributeError as e:
            return False

        