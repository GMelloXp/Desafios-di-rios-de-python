# Dia 5 · Lógica: encontre o maior movimento
Tempo: 10–20 minutos

## Objetivo: combinar for e if para encontrar o maior valor e lidar com empates.
### O desafio
Um prédio registrou a quantidade de encomendas recebidas em cinco dias. Crie um programa que:
1. Leia a quantidade de encomendas de cada dia.
2. Mostre a maior quantidade registrada.
3. Informe em qual dia ela ocorreu. Se houver empate, mantenha o primeiro dia.
Considere entradas inteiras e não negativas. Resolva usando variáveis, for e if, sem listas ou max().
## Conceito
Para encontrar o maior valor, mantenha um “maior até agora”. Cada nova entrada é comparada com esse valor. Se for maior, atualize tanto a quantidade quanto o dia correspondente.

Diferentemente de um acumulador, você não soma os valores: guarda o melhor resultado encontrado.

## Casos para conferir
| Entradas dos dias 1 a 5| Maior quantidade| Dia esperado |
| -------- | -------- | -------- |
| 12, 18, 9, 18, 7  | 18  | 2 |
| 20, 15, 10, 5, 0 | 20  | 1  |
| 1, 2, 3, 4, 5| 5 | 5 |


### Dica 1:
leia o primeiro dia antes do laço e use essa entrada como maior valor inicial. Depois, percorra os dias restantes com range(2, 6).

### Dica 2:
use > para atualizar o recorde. Com >=, um empate substituiria o primeiro dia pelo mais recente.
