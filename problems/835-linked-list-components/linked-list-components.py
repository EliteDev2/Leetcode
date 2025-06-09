# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        while head:
            temp_count = 0
            while head and head.val in num_set:
                temp_count = 1
                head = head.next
            count += temp_count
            if head:
                head = head.next
        return count    


        