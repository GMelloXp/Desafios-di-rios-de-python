
# Dia 9 · Problema aplicado: lista de tarefas pendentes
Tempo: 10–20 minutos

## Objetivo: 
guardar várias entradas em uma lista e exibi-las ao final.

### Conceito
Uma lista armazena vários valores em ordem:

tarefas = []
tarefas.append("Revisar cadastro")

[] cria uma lista vazia, .append() adiciona um item ao final e len(tarefas) informa quantos itens existem. Um for pode percorrer diretamente os itens da lista.

## Seu desafio
Crie um programa para registrar tarefas de um turno:
1. Peça uma tarefa por vez, removendo espaços das extremidades.
2. Encerre quando a pessoa digitar fim, aceitando também FIM, Fim etc.
3. Ignore entradas vazias e continue pedindo tarefas.
4. Guarde as tarefas válidas, preservando sua escrita e ordem.
5. Ao terminar, mostre a quantidade e cada tarefa em uma linha. Se nenhuma foi registrada, mostre Nenhuma tarefa registrada.
O comando fim não deve entrar na lista. Tarefas repetidas podem ser mantidas.

## Dica 1: 
leia a primeira tarefa antes do while. Continue enquanto tarefa.lower() != "fim". A comparação deve ser de igualdade, não uma busca com in.

## Dica 2: 
dentro do laço, adicione somente textos não vazios com .append(). Faça uma nova leitura em toda repetição, inclusive depois de uma entrada vazia.

| Entradas, em ordem | Resultado esperado |
| ------------------ | ------------------ |
|"", "Revisar cadastro", "fim"|  	1 tarefa: Revisar cadastro         |
|         "  Testar sistema  ", " FIM "          |   	1 tarefa: Testar sistema                 |
|          "Enviar relatório", "Enviar relatório", "fim"          |       2 tarefas iguais             |
|     "Conferir fim do turno", "fim"               |         	1 tarefa: Conferir fim do turno           |
|          "fim"         |           	Nenhuma tarefa registrada         |

Tente resolver e testar antes de consultar a solução.

