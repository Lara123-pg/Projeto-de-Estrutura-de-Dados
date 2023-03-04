print('''
Seja bem-vindo a lanchonete, abaixo temos as opções do nosso cardápio

1 - Batata frita
2 - Sanduíche com bacon
3 - Sanduíche com frango
4 - Sanduíche com carne
5 - Refrigerante
''')
      
opcoesCardapio = [1, 2, 3, 4, 5]
cardapio = ['Batata frita', 'Sanduíche com bacon', 'Sanduíche com frango', 'Sanduíche com carne', 'Refrigerante']

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
        print('Não temos essa opção no cardápio, por favor selecione opções entre 1 a 5')
        print('------------------------------------------------------------------------')

        return
    
    print(cardapio[adicionarPedido])
    print('------------------------')

    return 'Pedido feito'

while True:
    pedido = int(input('Digite a opção para pedir ou -1 para finalizar: '))

    if (pedido == -1):
        break
    
    fazerPedido = fazer_pedido(pedido)

    print(fazerPedido)