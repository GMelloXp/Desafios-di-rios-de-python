# Dia 6 · Problema aplicado: controle de estoque
Tempo: 10–20 minutos

## Objetivo: combinar repetição e condicionais para atualizar um estoque sem permitir saldo negativo.

## O desafio
Crie um programa que leia o estoque inicial de um produto e processe três pedidos de venda, um por vez.

Para cada pedido:
- Se a quantidade solicitada for menor ou igual ao estoque disponível, aprove a venda e desconte a quantidade.
- Caso contrário, recuse a venda sem alterar o estoque.
- Mostre o estoque restante após cada tentativa.
Ao final, informe quantas vendas foram aprovadas.

Considere estoque inicial inteiro e não negativo, e pedidos inteiros maiores que zero. Não é necessário tratar texto ou números inválidos nesta atividade.

### Conceito
Uma variável pode representar um estado que muda durante a execução. Aqui, estoque guarda a quantidade disponível naquele momento, não apenas a quantidade inicial.

Já um contador, como vendas_aprovadas, aumenta em 1 a cada venda aceita — independentemente de quantas unidades foram vendidas.


## Casos para conferir
Estoque inicial	| Três pedidos |	Resultado das vendas |	Estoque final |	Aprovadas |
| ------------ | ---------------- | ----------------- | ---------------- | -------- |
10 |	4, 8, 6 |	Aprova, recusa, aprova |	0 |	2 |
5 |	5, 1, 1 |	Aprova, recusa, recusa |	0 |	1 |
0 |	1, 2, 3 |	Recusa, recusa, recusa |	0 |	0 |
12 |	2, 3, 4 |	Aprova, aprova, aprova |	3 |	3 |


### Dica 1:
use for pedido in range(1, 4) e compare cada quantidade com o estoque atualizado.

### Dica 2:
tanto o desconto do estoque quanto o incremento do contador devem ficar dentro do bloco que aprova a venda.
