class Node:
    def __init__(self, v):
        self._next = None
        self._value = v

    @property
    def next(self):
        return self._next

    @next.setter
    def set_next(self, n):
        self._next = Node(n)

    @property
    def get_value(self):
        return int(self._value)
