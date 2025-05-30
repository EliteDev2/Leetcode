# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        cur = head

        while cur:
            if cur.val not in nums:
                tail.next = cur
                tail = tail.next
            cur = cur.next
        
        tail.next = None
        return dummy.next

        