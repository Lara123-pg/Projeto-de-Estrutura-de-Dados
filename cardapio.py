from stuctures import *
from rich.console import Console

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

def menu2():
    print('''
Agora que seu pedido foi finalizado, pode selecionar as opções abaixo:

1 - Mostrar pedido
2 - Mostrar pedido em formato de lista encadeada
3 - Adicionar pedido
4 - Remover pedido
    ''')

print('Seja bem-vindo a lanchonete, abaixo temos as opções do nosso cardápio')

menu()

opcoesCardapio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cardapio = ['Batata frita', 'Sanduíche de bacon', 'Sanduíche de frango', 'Sanduíche de carne', 'Sanduíche de queijo', 'Refrigerante', 'Suco','Sorvete', 'Bolo', 'Torta']

console = Console()

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


pedidos = Lanchonete()

def outrasOpcoes():
    menu2()

    while True:
        opcao = int(input('Digite a opção escolhida ou digite -1 para finalizar: '))
        print('')

        if (opcao == -1):
            break

        if (opcao == 1):
            pedidos.mostrarPedido()
            print('')
        
        elif (opcao == 2):
            pedidos.mostrarPedidoLinkedList()
            print('')
        
        elif (opcao == 3):
            menu()
            
            print('')
            novoPedido = int(input('Digite a opção do novo pedido que vai ser adicionado: '))

            buscaNovoPedido = busca_pedido(opcoesCardapio, novoPedido)
            pedidos.adicionarPedido(cardapio[buscaNovoPedido])

            console.print(f'[bold cyan]{cardapio[buscaNovoPedido]}[/bold cyan] foi selecionado.')
            print('-------------------------------')
            print('')

            menu2()
        
        else:
            print('')
            pedidos.mostrarPedido()
            print('')

            pedidoRemover = int(input('Digite o índice da opção que deseja remover: '))
            pedidos.removerPedido(pedidoRemover)

            print('')
            menu2()

    return
    
while True:
    pedido = int(input('Digite a opção para pedir ou -1 para finalizar: '))

    if (pedido == -1):
        print('Pedido finalizado')
        print('')

        outrasOpcoes()

        break
    
    fazerPedido = fazer_pedido(pedido)
    
    if fazerPedido != None:
        pedidos.adicionarPedido(fazerPedido)

        console.print(f'[bold cyan]{fazerPedido}[/bold cyan] foi selecionado.')
        print('-------------------------------')
        print('')

print('')
pedidos.mostrarPedido()