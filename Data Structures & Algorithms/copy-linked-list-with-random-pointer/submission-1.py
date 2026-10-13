"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hm = dict()
        old = head
        new = Node(head.val)
        dummy = Node(0, new, None)

        while old:
            new.val = old.val
            new.next = Node(0, None, None) if old.next else None
            hm[old] = new

            old = old.next
            new = new.next
        
        old = head
        new = dummy.next
        while old:
            new.random = hm.get(old.random, None)
            old = old.next
            new = new.next

        return dummy.next