# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0, None)
        remain = 0
        dummy = ListNode(0, res)

        while l1 or l2 or remain:
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0
            cur_s = l1_val + l2_val + remain
            if cur_s > 9:
                remain = 1
                cur_s %= 10
            else:
                remain = 0
            res.val = cur_s
            
            if l1 or l2 or remain:
                res.next = ListNode(0, None)

            res = res.next

        

        return dummy.next