# Dia 7 · Fundamentos: cadastro com while
Tempo: 10–20 minutos

## Objetivo:
repetir uma entrada até receber um nome preenchido, usando while e .strip().

## Conceito
O for é útil quando sabemos quantas repetições queremos. Já o while repete um bloco enquanto uma condição for verdadeira.

O método .strip() remove espaços das extremidades de um texto. Assim, uma entrada contendo apenas espaços vira "", uma string vazia.

## Seu desafio
Crie um programa que solicite o nome de um visitante.
1. Remova os espaços do início e do fim.
2. Se o resultado estiver vazio, mostre Nome obrigatório. Tente novamente. e peça o nome outra vez.
3. Repita até receber um nome não vazio.
4. Mostre o nome cadastrado e quantas entradas vazias foram recusadas.
Não é necessário verificar sobrenome ou restringir caracteres. Neste exercício, qualquer texto não vazio após .strip() é aceito.

## Casos para conferir
As aspas abaixo apenas delimitam as entradas; não devem ser digitadas.

| Entradas, em ordem | Nome cadastrado |	Recusadas |
| "Gabriel" |	Gabriel |	0 |
| "  Ana  " | Ana | 0 |
| "", "   ", "Bruno" |	Bruno |	2 |
| "  Maria Clara  " | Maria Clara |	0 |

### Dica 1:
leia o nome antes do laço. Use while nome == "": para repetir enquanto ele estiver vazio.

### Dica 2:
dentro do laço, incremente o contador e leia o nome novamente. Sem uma nova leitura, a condição continuará verdadeira e o programa ficará preso na repetição.

Tente implementar e executar os quatro testes antes de conferir a solução.

### Extra opcional:
exija pelo menos três caracteres após remover os espaços das extremidades. Use len(nome) para consultar o tamanho e ajuste a mensagem de erro.
