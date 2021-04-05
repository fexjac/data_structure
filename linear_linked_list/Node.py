class Node(object):
    def __init__(self, value=None, next= None):
        self.next = next
        self.value = value


    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next
