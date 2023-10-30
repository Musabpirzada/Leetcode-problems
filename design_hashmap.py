class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000  # Choose an initial size for the array of buckets
        self.buckets = [None] * self.size

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = ListNode(key, value)
        else:
            current = self.buckets[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if not current.next:
                    break
                current = current.next
            current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        current = self.buckets[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                return
            prev = current
            current = current.next

# Example usage:
myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
print(myHashMap.get(1))    # Output: 1
print(myHashMap.get(3))    # Output: -1
myHashMap.put(2, 1)
print(myHashMap.get(2))    # Output: 1
myHashMap.remove(2)
print(myHashMap.get(2))    # Output: -1
