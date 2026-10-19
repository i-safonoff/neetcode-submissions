# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_tail = dummy

        while True:
            node = prev_tail
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next
            
            cur_head = prev_tail.next
            
            prev = None
            cur = cur_head

            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            prev_tail.next = prev
            cur_head.next = cur
            prev_tail = cur_head

        return dummy.next

                
                
