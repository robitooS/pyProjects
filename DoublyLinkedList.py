class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList():
    def __init__ (self):
        self.head = None
        self.tail = None
        
    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        
    def add_to_end(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        
    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
            
        return removed_value
    
    def remove_from_end(self):
        if not self.tail:
            return None
        removed_value = self.tail.value
        self.tail = self.tail.prev
        
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
            
        return removed_value
    
def test_doubly_linked_list():
    # Criação da lista
    dll = DoublyLinkedList()
    
    # Teste 1: Adicionar ao início
    print("Teste 1: Adicionar ao início")
    dll.add_to_front(10)
    dll.add_to_front(20)
    dll.add_to_front(30)
    
    # Esperado: 30 -> 20 -> 10
    print("Lista após adicionar ao início:", end=" ")
    current = dll.head
    while current:
        print(current.value, end=" <-> " if current.next else "")
        current = current.next
    print()

    # Teste 2: Adicionar ao final
    print("Teste 2: Adicionar ao final")
    dll.add_to_end(40)
    dll.add_to_end(50)
    
    # Esperado: 30 -> 20 -> 10 -> 40 -> 50
    print("Lista após adicionar ao final:", end=" ")
    current = dll.head
    while current:
        print(current.value, end=" <-> " if current.next else "")
        current = current.next
    print()

    # Teste 3: Remover do início
    print("Teste 3: Remover do início")
    removed_value = dll.remove_from_front()
    
    # Esperado: Remover 30
    print("Valor removido:", removed_value)  # Deve ser 30
    print("Lista após remover do início:", end=" ")
    current = dll.head
    while current:
        print(current.value, end=" <-> " if current.next else "")
        current = current.next
    print()

    # Teste 4: Remover do final
    print("Teste 4: Remover do final")
    removed_value = dll.remove_from_end()
    
    # Esperado: Remover 50
    print("Valor removido:", removed_value)  # Deve ser 50
    print("Lista após remover do final:", end=" ")
    current = dll.head
    while current:
        print(current.value, end=" <-> " if current.next else "")
        current = current.next
    print()

    # Teste 5: Remover todos os elementos
    print("Teste 5: Remover todos os elementos")
    
    while dll.head is not None:
        removed_value = dll.remove_from_front()
        print("Valor removido:", removed_value)

# Executar os testes
test_doubly_linked_list()
        