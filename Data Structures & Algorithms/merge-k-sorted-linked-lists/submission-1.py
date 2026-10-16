# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        dummy = ListNode()
        cur = dummy
        i = -1

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))
        
        while h:
            _, i, node = heapq.heappop(h)
            
            cur.next = node
            lists[i] = lists[i].next
            if lists[i] != None:
                heapq.heappush(h, (lists[i].val, i, lists[i]))
            cur = cur.next
        return dummy.next


