
# Dia 7 · Fundamentos: cadastro com while
# Tempo: 10–20 minutos
# Objetivo: repetir uma entrada até receber um nome preenchido, usando while e .strip().
# Conceito
# O for é útil quando sabemos quantas repetições queremos. Já o while repete um bloco enquanto uma condição for verdadeira.

# O método .strip() remove espaços das extremidades de um texto. Assim, uma entrada contendo apenas espaços vira "", uma string vazia.
# Seu desafio
# Crie um programa que solicite o nome de um visitante.
# 1. Remova os espaços do início e do fim.
# 2. Se o resultado estiver vazio, mostre Nome obrigatório. Tente novamente. e peça o nome outra vez.
# 3. Repita até receber um nome não vazio.
# 4. Mostre o nome cadastrado e quantas entradas vazias foram recusadas.

nome_visitante = input("Digite o nome do visitante: ").strip()
tentativa_recusada = 0


while nome_visitante == "" or len(nome_visitante) < 3:

    print("Nome Inválido. Tente novamente!")
    nome_visitante = input("Digite o nome do visitante: ").strip()
    tentativa_recusada += 1

print("Visitante cadastrado:", nome_visitante)
print("Tentativas recusadas:", tentativa_recusada)
