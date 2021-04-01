from Node import Node

class List:

    def __init__(self):
        self.head = None

    def insert(self, v):
        NewNode = Node(v)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.set_next = NewNode

    def listprint(self):
        print_value = self.head
        while print_value is not None:
            print (print_value.get_value)
            print_value = print_value.next

''''
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
