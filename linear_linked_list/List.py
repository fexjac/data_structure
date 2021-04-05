from Node import Node

class List:

    def __init__(self):
        self.head = None

    def __len__(self):
        return 0

    def insert(self, v):
        new_node = Node(v)

        if self.head is None:
            self.head = new_node
            return
        else:
            temp_node = self.head
            while(temp_node.get_next() != None):
                temp_node = temp_node.get_next()
            temp_node = temp_node.set_next(new_node)


    def print_list(self):
        pr = self.head
        while pr is not None:
            temp_print = int(pr.get_value())
            print(temp_print)
            print("->")
            pr = pr.get_next()
        print("")


'''
    public boolean remover(int v){
      Node prox = head;
      if(prox.getValor() == v){
        head = prox.getProx();
        return true;
      }

      while(prox.getProx()!=null &&prox.getProx().getValor()!=v){
        prox = prox.getProx();
      }

      if(prox.getProx()==null){
        return false;
      }

      if (prox.getProx().getValor() == v){
        prox.setProx(prox.getProx().getProx());
      }
      return true;

    }



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
