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
            temp_node = temp_node.set_next(new_node)
            self.counter = self.counter + 1


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
'''

    public boolean busca(int v){
      Node pr = head;
      while(pr != null){
        if (pr.getValor()==v){
          return true;
        }
        pr = pr.getProx();
      }
      return false;
    }

    public int tamanho(){
      int tam = 0;
      Node prox = head;
      if (prox == null){
        return tam;
      }else{
        while(prox!=null){
          tam = tam + 1;
          prox = prox.getProx();
        }
        return tam;
'''
