# Dia 8 · Lógica: conte chamados por palavra-chave
Tempo: 10–20 minutos

## Objetivo: 
percorrer textos e contar correspondências sem diferenciar maiúsculas de minúsculas.

### Conceito
O operador in verifica se um trecho aparece em um texto:
"erro" in "erro ao entrar"  # True
A comparação diferencia maiúsculas de minúsculas. Use .lower() para converter o texto para minúsculas antes de comparar.

## Seu desafio
Crie um programa que leia cinco descrições de chamados de suporte e informe quantas contêm o trecho "erro".

### Regras:
1. Aceite qualquer combinação de maiúsculas e minúsculas.
2. Conte cada chamado apenas uma vez, mesmo que "erro" apareça várias vezes.
3. Conte o trecho em qualquer posição: "erros" também deve corresponder.
4. Uma descrição vazia não conta.
Use for, if e um contador. Não é necessário guardar as descrições em uma lista.

### Dica 1: 
comece com um contador igual a zero e leia cada descrição dentro de for numero in range(1, 6).

### Dica 2: 
teste if "erro" in descricao.lower(): e incremente o contador em 1, não pela quantidade de ocorrências.

Tente resolver e executar os testes antes de continuar.

## Casos para conferir
|Cinco descrições |	Contagem esperada |
| --------------- | ----------------- |
|"Erro", "ERRO", "erro", "ErRo", "erros" |	5 |
|"Erro e erro", "Acesso", "Monitor", "", "Cadastro" |	1 |
|"Acesso", "Monitor", "Cadastro", "", "Rede lenta" |	0 |