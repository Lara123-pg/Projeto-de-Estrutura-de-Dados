class Pedido:
    def __init__(self, pedido):
        self.pedido = pedido
        self.next = None
        self.previous = None

class Lanchonete:
    def __init__(self):
        self.head = None
        self.size = 0

    def adicionarPedido(self, novoPedido):
        novoPedido = Pedido(novoPedido)

        self.size += 1

        if (self.head == None):
            self.head = novoPedido

            return
        
        current = self.head

        while (current.next != None):
            current = current.next

        current.next = novoPedido
        current.next.previous = current

    def removerPedido(self, index):
        if (self.head == None or index > self.size):
            return 'Não é possível remover pedido.'

        elif (index == 0):
            self.head = self.head.next
            self.head.previous = None
        
            return
        
        current = self.head
        count = 1

        while (current != None):
            if (count == index):
                current.previous = current.next
                current.next = current.previous

                return 'Pedido removido.'

            current = current.next
            count += 1

    def mostrarPedidoLinkedList(self):
        current = self.head

        print('Pedido')

        while (current != None):
            print('-----------------------------')
            print(f'Pedido atual: {current.pedido}')

            if (current.previous != None):
                print(f'Pedido anterior: {current.previous.pedido}')

            if (current.next != None):
                print(f'Próximo pedido: {current.next.pedido}')

            current = current.next
    
    def mostrarPedido(self):
        current = self.head

        print('Pedido')
        print('-----------------------------')
        
        while (current != None):
            print(current.pedido)

            current = current.next