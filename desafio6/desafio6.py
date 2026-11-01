# Dia 6 · Problema aplicado: controle de estoque
# Tempo: 10–20 minutos
# Objetivo: combinar repetição e condicionais para atualizar um estoque sem permitir saldo negativo.
# O desafio
# Crie um programa que leia o estoque inicial de um produto e processe três pedidos de venda, um por vez.

# Para cada pedido:
# - Se a quantidade solicitada for menor ou igual ao estoque disponível, aprove a venda e desconte a quantidade.
# - Caso contrário, recuse a venda sem alterar o estoque.
# - Mostre o estoque restante após cada tentativa.
# Ao final, informe quantas vendas foram aprovadas.

# Considere estoque inicial inteiro e não negativo, e pedidos inteiros maiores que zero. Não é necessário tratar texto ou números inválidos nesta atividade.


estoque_inicial = int(input("Digite a quantidade do estoque inicial do produto: "))
estoque_disponivel = estoque_inicial
vendas_aprovadas = 0
print("Estoque inicial: ", estoque_inicial)
for pedido in range (1,4):

  quantidade_pedido = int(input(f"Quantidade do pedido {pedido}: "))

  if quantidade_pedido <= estoque_disponivel:
    vendas_aprovadas += 1
    estoque_disponivel -= quantidade_pedido
    print("Venda Aprovada!")
    print("Estoque disponível: ", estoque_disponivel)
  else:
    print("Venda recusada: Estoque Insuficiente!")
    print("Estoque disponível: ", estoque_disponivel)

print()
print("Vendas aprovadas: ", vendas_aprovadas)
