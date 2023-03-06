def menu():
    print('''
    Cardápio

    1 - Batata frita
    2 - Sanduíche de bacon
    3 - Sanduíche de frango
    4 - Sanduíche de carne
    5 - Sanduíche de queijo
    6 - Refrigerante
    7 - Suco
    8 - Sorvete
    9 - Bolo
    10 - Torta
    ''')

print('Seja bem-vindo a lanchonete, abaixo temos as opções do nosso cardápio')

menu()

opcoesCardapio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cardapio = ['Batata frita', 'Sanduíche de bacon', 'Sanduíche de frango', 'Sanduíche de carne', 'Sanduíche de queijo', 'Refrigerante', 'Suco','Sorvete', 'Bolo', 'Torta']

def busca_pedido(opcoes, op):
    left = 0
    right = len(opcoes) - 1

    while (left <= right):
        middle = (left + right) // 2

        if (op == opcoes[middle]):
            return middle

        elif (op > opcoes[middle]):
            left = middle + 1
        
        else:
            right = middle - 1
    
    return -1 

def fazer_pedido(pedido):
    adicionarPedido = busca_pedido(opcoesCardapio, pedido)

    if (adicionarPedido == -1):
        print('Não temos essa opção no cardápio, por favor selecione opções entre 1 e 10')
        print('-------------------------------------------------------------------------')

        return

    return cardapio[adicionarPedido]

class Pedido:
    def __init__(self, pedido):
        self.pedido = pedido
        self.next = None
        self.previous = None

class Lanchonete:
    def __init__(self):
        self.pedidoAtual = None

    def adicionarPedido(self, novoPedido):
        novoPedido = Pedido(novoPedido)

        if (self.pedidoAtual == None):
            self.pedidoAtual = novoPedido

            return
        
        current = self.pedidoAtual

        while (current.next != None):
            current = current.next

        current.next = novoPedido
        current.next.previous = current

    def mostrarPedidoLinkedList(self):
        current = self.pedidoAtual

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
        current = self.pedidoAtual

        print('Pedido')
        print('-----------------------------')
        
        while (current != None):
            print(current.pedido)

            current = current.next


pedidos = Lanchonete()

while True:
    pedido = int(input('Digite a opção para pedir ou -1 para finalizar: '))

    if (pedido == -1):
        print('Pedido finalizado')
        print('')

        break
    
    fazerPedido = fazer_pedido(pedido)
    pedidos.adicionarPedido(fazerPedido)

    print(fazerPedido)
    print('')

pedidos.mostrarPedido()