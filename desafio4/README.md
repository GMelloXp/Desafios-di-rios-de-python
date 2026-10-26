# Dia 4 · Fundamentos: somando horas de estudo
⏱️ 10–20 minutos
Objetivo: aprender for, range() e o padrão de acumulação.
Conceito
Um laço for repete um bloco de código. Com range(1, 6), por exemplo, a variável de controle assume os valores de 1 a 5.

Para somar valores recebidos durante as repetições, criamos um acumulador:

total = 0
total = total + novo_valor

A forma abreviada da segunda linha é:
total += novo_valor

Seu desafio
Crie um programa que registre o tempo estudado durante cinco dias.

O programa deve:
1. Solicitar a quantidade de minutos estudados em cada um dos cinco dias.
2. Calcular o total de minutos estudados.
3. Calcular a média diária.
4. Converter o total para horas e minutos.
5. Informar se a meta de 300 minutos foi alcançada.
Considere entradas inteiras e não negativas.

Casos para conferir
| Minutos nos cinco dias| Total| Horas e minutos| Média | Resultado |
| -------- | -------- | -------- | -------- | -------- |
| 60, 45, 90, 30, 75  | 300  | 5h 0min  | 60,0 | Meta alcançada
| 30, 30, 30, 30, 30 | 150   | 2h 30min  | 30,0 | Faltaram 150 minutos
| 61, 0, 0, 0, 0 | 61 | 1h 1min | 12,2 | Faltaram 239 minutos |