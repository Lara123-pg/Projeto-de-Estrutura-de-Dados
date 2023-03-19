class Pedido:
    def __init__(self, pedido):
        self.pedido = pedido
        self.quantidade = 0
        self.next = None
        self.previous = None

class Lanchonete:
    def __init__(self):
        self.head = None
        self.size = 0

    def quantidadePedidos(self, pedidos):
        current = self.head

        while (current != None):
            if current.pedido == pedidos:
                current.quantidade += 1

                return True
            
            current = current.next
        
        return False
    
    def adicionaQuantidadePedidos(self, pedidos):
        current = self.head

        while (current.next != None):
            if current.next.pedido == pedidos.pedido:
                current.next.quantidade += 1

                return

            current = current.next

    def adicionarPedido(self, novoPedido):
        novoPedido = Pedido(novoPedido)
        current = self.head

        repetPedido = self.quantidadePedidos(novoPedido.pedido)

        if repetPedido:
            return
        
        self.size += 1

        if (self.head == None):
            self.head = novoPedido
            self.head.quantidade += 1

            return

        while (current.next != None):
            current = current.next

        current.next = novoPedido
        current.next.previous = current

        self.adicionaQuantidadePedidos(novoPedido)

    def removerPedido(self, index):
        index = index - 1

        if (self.head == None or index > self.size):
            print('Não é possível remover esse pedido.')

            return

        elif (index == 0):
            current = self.head

            if (current.quantidade) == 1:
                if (self.head.next != None):
                    self.head = self.head.next
                    self.head.previous = None
                
                else:
                    self.head = None

                print('Pedido removido.')
                print('')
            
            else:
                current.quantidade -= 1
            
            return
        
        previous = self.head
        current = self.head.next
        count = 1

        while (count <= index):
            if (current.next == None):
                if (current.quantidade == 1):
                    previous.next = None
                
                else:
                    current.quantidade -= 1

                print('Pedido removido.')
                print('')
            
            else:
                if count == index:
                    if (current.quantidade == 1):
                        previous.next = current.next
                        current.next.previous = current.previous

                    else:
                        current.quantidade -= 1

                    print('Pedido removido.')
                    print('')

                    return

            previous = current
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
        count = 1

        print('Pedido')
        print('-----------------------------')
        
        while (current != None):
            print(f'{count} - {current.pedido} ({current.quantidade})')

            current = current.next
            count += 1