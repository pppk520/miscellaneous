class DListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.d = {}
        self.head = None
        self.tail = None
        self.capacity = capacity

    def update_list(self, key):
        node = self.d[key]

        if len(self.d) == 1:
            return

        if node == self.tail:
            return

        if node == self.head:
            self.head = node.next

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        node.next = None

    def print_list(self):
        node = self.head
        ll = []
        while node:
            ll.append('(%s, %s)' %(node.key, node.val))
            node = node.next

        print('List: %s' %' --> '.join(ll))

    # @return an integer
    def get(self, key):
        if not key in self.d:
            return -1                

        self.update_list(key)

        return self.d[key].val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if not key in self.d:
            self.d[key] = DListNode(key, value)

            if self.tail:
                node = self.d[key]
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                self.tail.next = None
            else:
                self.head = self.d[key]
                self.tail = self.head                

            if len(self.d) > self.capacity:
                del self.d[self.head.key]

                self.head = self.head.next
                self.head.prev = None
        else:
            if len(self.d) == 1:
                self.d[key].val = value
                return self.d[key].val

            self.update_list(key)
            self.d[key].val = value


if __name__ == '__main__':
    lru_cache = LRUCache(1)
    lru_cache.set(2, 1)
    lru_cache.set(2, 2)
    print(lru_cache.get(2) == 2)
    lru_cache.set(1, 1)
    lru_cache.set(4, 1)
    print(lru_cache.get(2) == -1)



    '''
    lru_cache = LRUCache(11)
    lru_cache.set(9, 1)
    print(lru_cache.get(12))
    lru_cache.set(8, 3)
    print(lru_cache.get(7))
    print(lru_cache.get(11))
    print(lru_cache.get(9))
    lru_cache.set(13, 12)
    print(lru_cache.get(11))
    print(lru_cache.get(1))
    lru_cache.set(8, 14)
    print(lru_cache.get(2))
    print(lru_cache.get(14))
    print(lru_cache.get(11))
    lru_cache.set(11, 10)
    lru_cache.set(10, 6)
    print(lru_cache.get(3))
    print(lru_cache.get(3))
    print(lru_cache.get(12))
    print(lru_cache.get(7))
    print(lru_cache.get(2))
    print(lru_cache.get(11))
    lru_cache.set(11, 14)
    lru_cache.set(11, 12)
    lru_cache.set(3, 15)
    print(lru_cache.get(14))
    print(lru_cache.get(6))
    print(lru_cache.get(4))
    lru_cache.set(13, 3)
    print(lru_cache.get(11))
    lru_cache.set(4, 15)
    print(lru_cache.get(12))
    print(lru_cache.get(9))
    lru_cache.set(15, 9)
    print(lru_cache.get(4))
    lru_cache.set(5, 15)
    lru_cache.set(4, 4)
    lru_cache.set(9, 7)
    print(lru_cache.get(5))
    lru_cache.set(9, 13)
    lru_cache.set(11, 10)
    lru_cache.set(11, 12)
    print(lru_cache.get(12))
    lru_cache.set(7, 6)
    lru_cache.set(6, 2)
    print(lru_cache.get(1))
    lru_cache.set(15, 6)
    print(lru_cache.get(7))
    lru_cache.set(8, 8)
    lru_cache.set(14, 8)
    print(lru_cache.get(12))
    print(lru_cache.get(12))
    lru_cache.set(6, 15)
    print(lru_cache.get(2))
    lru_cache.set(2, 5)
    lru_cache.set(13, 15)
    print(lru_cache.get(13))
    lru_cache.set(6, 6)
    print(lru_cache.get(7))
    print(lru_cache.get(12))
    print(lru_cache.get(15))
    lru_cache.set(10, 8)
    print(lru_cache.get(6))
    print(lru_cache.get(5))
    print(lru_cache.get(5))
    lru_cache.set(14, 10)
    print(lru_cache.get(15))
    print(lru_cache.get(5))
    print(lru_cache.get(14))
    print(lru_cache.get(12))
    lru_cache.set(11, 15)
    print(lru_cache.get(5))
    print(lru_cache.get(2))
    lru_cache.set(9, 5)
    lru_cache.set(4, 7)
    print(lru_cache.get(13))
    print(lru_cache.get(2))
    lru_cache.set(7, 13)
    print(lru_cache.get(9))
    print(lru_cache.get(9))
    lru_cache.set(11, 5)
    print(lru_cache.get(6))
    print(lru_cache.get(4))
    lru_cache.set(6, 13)
    print(lru_cache.get(2))
    lru_cache.set(3, 15)
    print(lru_cache.get(13))
    print(lru_cache.get(4))
    lru_cache.set(6, 11)
    print(lru_cache.get(15))
    print(lru_cache.get(15))
    print(lru_cache.get(3))
    print(lru_cache.get(3))
    print(lru_cache.get(3))
    '''

