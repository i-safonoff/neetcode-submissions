class ListNode:
    def __init__(self, key=None, value=None, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = {}

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        res = self.m[key].value

        old = self.m[key]
        old.prev.next, old.next.prev = old.next, old.prev
        del(self.m[key])
            
        node = ListNode(key, res, self.tail, self.tail.prev)
        self.tail.prev.next, self.tail.prev = node, node
        self.m[key] = node

        return res


    def put(self, key: int, value: int) -> None:
        if key in self.m:
            node = self.m[key]
            node.value = value

            node.prev.next = node.next
            node.next.prev = node.prev

            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node
            return

        if len(self.m) == self.capacity:
            lru = self.head.next

            lru.prev.next = lru.next
            lru.next.prev = lru.prev
            del self.m[lru.key]

        node = ListNode(key, value)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.m[key] = node
