print('Seja bem-vindo a lanchonete, abaixo temos as opções do nosso cardápio')

opcoesCardapio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cardapio = ['Batata frita', 'Sanduíche de bacon', 'Sanduíche de frango', 'Sanduíche de carne', 'Sanduíche de queijo', 'Refrigerante', 'Suco','Sorvete', 'Bolo', 'Torta']

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
    
    print(cardapio[adicionarPedido])
    print('-----------------------')

    return 'Pedido anotado'

while True:
    menu()

    pedido = int(input('Digite a opção para pedir ou -1 para finalizar: '))

    if (pedido == -1):
        print('Pedido finalizado')

        break
    
    fazerPedido = fazer_pedido(pedido)

    print(fazerPedido)
    print('')