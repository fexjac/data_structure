class Node(object):
    def __init__(self, value=None, next= None):
        self._next = next
        self._value = value

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def set_next(self, new_next):
        self._next = new_next
