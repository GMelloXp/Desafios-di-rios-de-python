
"""

Seu desafio
Crie um programa que:
1. Peça o nome de uma assinatura, seu valor mensal e o orçamento disponível.
2. Se o valor for menor ou igual ao orçamento, informe quanto sobra.
3. Caso contrário, informe quanto falta.
Considere valores não negativos e entradas numéricas válidas. Digite decimais com ponto, como 29.90. Mostre os valores com duas casas decimais.

"""

nome_assinatura = input("Digite o nome da assinatura: ")
valor_mensal_assinatura = float(input("Qual o valor mensal da assinatura? "))
orcamento_disponivel = float(input("Qual o orçamento disponível? "))


if valor_mensal_assinatura <= orcamento_disponivel:
  sobra_dinheiro = orcamento_disponivel - valor_mensal_assinatura
  print(f"Nome da assinatura: {nome_assinatura}\n"
        f"Valor mensal: {valor_mensal_assinatura:.2f}\n"
        f"Orçamento disponível: {orcamento_disponivel:.2f}\n"
        f"{nome_assinatura} cabe no orçamento. Sobram  R${sobra_dinheiro:.2f}"
        )
else:
  falta_dinheiro = valor_mensal_assinatura - orcamento_disponivel
  print(f"Nome da assinatura: {nome_assinatura}\n"
          f"Valor mensal: {valor_mensal_assinatura:.2f}\n"
          f"Orçamento disponível: {orcamento_disponivel:.2f}\n"
          f"{nome_assinatura} não cabe no orçamento. Faltam R${falta_dinheiro:.2f}"
          )
