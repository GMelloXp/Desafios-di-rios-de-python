
"""
Seu desafio
Crie um programa que solicite:
1. Valor do pedido.
2. Se o cliente possui um cupom, respondendo S ou N.
Aplique estas regras:
- Se o cliente tiver cupom, conceda 10% de desconto.
- Depois do desconto, pedidos de R$ 100,00 ou mais recebem frete grátis.
- Nos demais pedidos, acrescente R$ 12,00 de frete.
- Exiba o desconto, o frete e o total final com duas casas decimais.
Considere valores positivos e respostas válidas.
"""

valor_pedido = float(input("Qual o valor do pedido? "))
possui_cupom = input("Possui cupom? (S/N) ").upper()


if possui_cupom == "S":
  valor_desconto = (valor_pedido * 0.1)
  valor_pedido_com_desconto = valor_pedido - valor_desconto
  if valor_pedido_com_desconto < 100:
    frete = 12.00
    valor_total_pedido = valor_pedido_com_desconto + frete
    print(
            f"Valor do pedido: R${valor_pedido:.2f}\n"
            f"Possui Cupom? (S/N): {possui_cupom}\n"
            f"Valor do desconto: R${valor_desconto:.2f}\n"
            f"Novo valor do pedido: R${valor_pedido_com_desconto:.2f}\n"
            f"Frete: R${frete:.2f}\n"
            f"Total final: R${valor_total_pedido:.2f}"
           )
  else:
    valor_total_pedido = valor_pedido_com_desconto
    frete = 0
    print(
            f"Valor do pedido: R${valor_pedido:.2f}\n"
            f"Possui Cupom? (S/N): {possui_cupom}\n"
            f"Valor do desconto: R${valor_desconto:.2f}\n"
            f"Novo valor do pedido: R${valor_pedido_com_desconto:.2f}\n"
            f"Frete: R${frete:.2f}\n"
            f"Total final: R${valor_total_pedido:.2f}"
          )

else:
  if valor_pedido < 100:
    frete = 12.00
    valor_total_pedido = valor_pedido + frete
    print(
          f"Valor do pedido: R${valor_pedido:.2f}\n"
          f"Possui Cupom? (S/N): {possui_cupom}\n"
          f"Frete: R${frete:.2f}\n"
          f"Total final: R${valor_total_pedido:.2f}"
         )
  else:
    frete = 0
    valor_total_pedido = valor_pedido + frete
    print(
          f"Valor do pedido: R${valor_pedido:.2f}\n"
          f"Possui Cupom? (S/N): {possui_cupom}\n"
          f"Frete: R${frete:.2f}\n"
          f"Total final: R${valor_total_pedido:.2f}"
         )
