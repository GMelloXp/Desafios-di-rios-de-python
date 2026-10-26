""" "
Seu desafio
Crie um programa que registre o tempo estudado durante cinco dias.

O programa deve:
1. Solicitar a quantidade de minutos estudados em cada um dos cinco dias.
2. Calcular o total de minutos estudados.
3. Calcular a média diária.
4. Converter o total para horas e minutos.
5. Informar se a meta de 300 minutos foi alcançada.
Considere entradas inteiras e não negativas.
"""

# iniciando o contador de minutos em 0
total_minutos = 0

# iniciando o loop for
for n in range(5):
    minutos_estudados = int(input(f"Quantos minutos você estudou no dia {n + 1}? "))
    total_minutos += minutos_estudados

# variáveis para calculo dos minutos totais e outros cálculos
horas_inteiras = total_minutos // 60
minutos_inteiros = total_minutos % 60
media_diaria = total_minutos / 5
meta_de_minutos_estudados = 300
minutos_faltantes = meta_de_minutos_estudados - total_minutos

# variáveis que mostram os resultados dos calculos
total_estudado = f"Total estudado: {total_minutos} minutos."
tempo_horas_minutos = (
    f"Equivalente a: {horas_inteiras} hora(s) e {minutos_inteiros} minuto(s)."
)
media_minutos_estudados = f"Média diária: {media_diaria:.2f} minutos."
meta_alcancada = (
    f"Meta mínima de {meta_de_minutos_estudados} minutos estudados, alcançada!"
)
meta_nao_alcancada = f"Meta não alcançada. Faltam {minutos_faltantes} minutos!"

# condicional para exibir qual cálculo será exibido
if total_minutos < meta_de_minutos_estudados:
    print(
        f"\n"
        f"{total_estudado}\n"
        f"{tempo_horas_minutos}\n"
        f"{media_minutos_estudados}\n"
        f"{meta_nao_alcancada}"
    )
else:
    print(
        f"\n"
        f"{total_estudado}\n"
        f"{tempo_horas_minutos}\n"
        f"{media_minutos_estudados}\n"
        f"{meta_alcancada}"
    )
