# Dia 8 · Lógica: conte chamados por palavra-chave
# Tempo: 10–20 minutos
# Objetivo: percorrer textos e contar correspondências sem diferenciar maiúsculas de minúsculas.
# Conceito
# O operador in verifica se um trecho aparece em um texto:
# "erro" in "erro ao entrar"  # True
# A comparação diferencia maiúsculas de minúsculas. Use .lower() para converter o texto para minúsculas antes de comparar.
# Seu desafio
# Crie um programa que leia cinco descrições de chamados de suporte e informe quantas contêm o trecho "erro".

# Regras:
# 1. Aceite qualquer combinação de maiúsculas e minúsculas.
# 2. Conte cada chamado apenas uma vez, mesmo que "erro" apareça várias vezes.
# 3. Conte o trecho em qualquer posição: "erros" também deve corresponder.
# 4. Uma descrição vazia não conta.
# Use for, if e um contador. Não é necessário guardar as descrições em uma lista.

contador_erro = 0

for n in range (1,6):
    descricao_chamado = input(f"Chamado {n}: ")
    
    if ("erro" or "erros") in descricao_chamado.lower():
        contador_erro += 1

print(f"Chamado {n}: {descricao_chamado}.")
print(f"Chamados com 'erro': {contador_erro} ")
    


