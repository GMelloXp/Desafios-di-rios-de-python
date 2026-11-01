# Dia 5 · Lógica: encontre o maior movimento
# Tempo: 10–20 minutos
# Objetivo: combinar for e if para encontrar o maior valor e lidar com empates.
# O desafio
# Um prédio registrou a quantidade de encomendas recebidas em cinco dias. Crie um programa que:
# 1. Leia a quantidade de encomendas de cada dia.
# 2. Mostre a maior quantidade registrada.
# 3. Informe em qual dia ela ocorreu. Se houver empate, mantenha o primeiro dia.
# Considere entradas inteiras e não negativas. Resolva usando variáveis, for e if, sem listas ou max()

qtd_encomendas_dia_inicial = int(input("Quantas encomendas recebidas no dia 1? "))
maior_qtd = qtd_encomendas_dia_inicial
dia_maior_qtd = 1

for n in range (2,6):
  qtd_encomendas_outros_dias = int(input(f"Quantas encomendas recebidas no dia {n}? "))
  if qtd_encomendas_outros_dias > maior_qtd:
    maior_qtd = qtd_encomendas_outros_dias
    dia_maior_qtd = n


print()
print(f"Maior quantidade de encomendas: {maior_qtd} encomendas.")
print(f"Primeiro dia com essa quantidade: {dia_maior_qtd}")
