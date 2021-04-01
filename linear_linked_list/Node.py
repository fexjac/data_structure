class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

    @next.setter
    def next(self, n):
        self._next = Node(n)

    @property
    def next(self):
        return self._next

    @property
    def value(self):
        return self._value
