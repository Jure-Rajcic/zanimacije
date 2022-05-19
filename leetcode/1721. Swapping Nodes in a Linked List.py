from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = [None] * 100000
        i = 0
        curr = head
        while curr:
            arr[i] = curr
            curr = curr.next
            i += 1
        arr[k - 1].val , arr[i - k].val = arr[i - k].val , arr[k - 1].val
        return head
