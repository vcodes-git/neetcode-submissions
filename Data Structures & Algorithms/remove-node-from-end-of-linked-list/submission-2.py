# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        head_cpy = head
        cur = head
        N = 0
        while cur:
            N+=1
            cur = cur.next
        if N == 1:
            return None
        prev = None

        if N-n == 0:
            return head_cpy.next
        for _ in range(N - n):
            prev = head
            head = head.next
        

        if prev:
            prev.next = head.next

        return head_cpy

        