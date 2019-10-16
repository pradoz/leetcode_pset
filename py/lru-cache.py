class Node:
    def __init__(self, k, v: int):
        ''' initiliazation of a Node for LRUCache '''
        # initialize the key and value of the node
        self.key = k
        self.val = v

        # pointers for the doubly-linked list
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, cap: int):
        self.capacity = cap
        self.dic = {}

        # linking the head/tail pointers
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        '''
        get() returns the value (will always be positive) of the key if
        the key exists in the cache, otherwise it returns -1.
        '''
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, k: int, val: int) -> None:
        '''
        put() - Set or insert the value if the key is not already
        present. When the cache reached its capacity, it should invalidate the
        least recently used item before inserting a new item.
        '''
        if k in self.dic:
            self._remove(self.dic[k])
        n = Node(k, val)
        self._add(n)
        self.dic[k] = n

        # check to see if we go over capacity
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]


    def _add(self, node: Node) -> None:
        '''
        helper function to rearrange pointers in the doubly-linked list when we
        add a Node to the cache
        '''
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


    def _remove(self, node: Node) -> None:
        '''
        helper function to rearrange pointers in the doubly-linked list when we
        remove a Node from the cache
        '''
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)