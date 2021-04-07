from Node import Node

class List:

    def __init__(self):
        self.head = None
        self.counter = 0

    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.counter = self.counter + 1
            return
        else:
            temp_node = self.head
            while(temp_node.get_next() is not None):
                temp_node = temp_node.get_next()
            temp_node.set_next(new_node)
            temp_node.set_before(temp_node)
            self.counter = self.counter + 1

    def insert_in_position(self, value, position):
        new_node = Node(value)

        if position > self.counter:
            print('Posicao indisponivel')
            return
        temp_node = self.head
        temp_position = 0

        while temp_position < position:
            temp_position = temp_position + 1
            temp_node = temp_node.get_next()

        new_node.set_next(temp_node)
        print(int(new_node.get_next().get_value()))
        new_node.set_before(temp_node.get_before())
        print(int(new_node.get_before().get_value()))
        temp_node.get_before().set_next(new_node)
        print(int(temp_node.get_next().get_value()))
        temp_node.set_before(new_node)
        print(int(temp_node.get_before().get_value()))

        '''
         novo.setProx(aux);
         novo.setAnt(aux.getAnt());
         aux.getAnt().setProx(novo);
         aux.setAnt(novo);
         '''
    def set_head(self, value):
        self.head = value
        self.counter = self.counter + 1

    def get_head(self):
        return self.head

    def print_list(self):
        print_item = self.head
        while print_item is not None:
            temp_print = int(print_item.get_value())
            print(temp_print)
            print_item = print_item.get_next()
        print("")

    def remove(self, value):
        temp_node = self.head

        if temp_node.get_value() == value:
            self.head = temp_node.get_next()
            self.counter = self.counter - 1
            return True

        while temp_node.get_next() is not None and temp_node.get_next().get_value() is not value:
            temp_node = temp_node.get_next()

        if temp_node.get_next() is None:
            return False

        if temp_node.get_next().get_value() is value:
            temp_node.set_next(temp_node.get_next().get_next())
            self.counter = self.counter - 1
        return True

    def get_counter(self):
        return int(self.counter)

    def search(self, value):
        temp_node = self.head
        while temp_node is not None:
            if temp_node.get_value() is value:
                return True
            temp_node = temp_node.get_next()
        return False
