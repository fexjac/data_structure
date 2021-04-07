class Node(object):
    def __init__(self, value=None, next= None, before=None):
        self.next = next
        self.before = before
        self.value = value

    def get_value(self):
        return int(self.value)

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_before(self):
        return self.before

    def set_before(self, new_before):
        self.before = new_before
