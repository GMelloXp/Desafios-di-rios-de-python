# Crie um programa de triagem para uma vaga de estágio em tecnologia. O programa deve solicitar:
# 1. A pontuação do candidato no teste técnico, de 0 a 100.
# 2. A porcentagem de presença no curso preparatório, de 0 a 100.
# Depois, classifique o candidato conforme estas regras:
# - Aprovado: pontuação igual ou superior a 70 e presença igual ou superior a 75.
# - Banco de talentos: pontuação igual ou superior a 50 e presença igual ou superior a 60, desde que não tenha sido aprovado.
# - Não selecionado: qualquer outro resultado.
# Considere que o usuário fornecerá números inteiros válidos.

nome = input("Digite o seu nome: ")
pontuacao_teste = int(input("Digite a sua pontuação(0 a 100): "))
porcentagem_presenca = int(input("Qual sua porcentagem de presença(0 a 100)? "))

#Vamos criar uma variável para cada situação, onde conterá as informações a serem exibidas.
#As situações poderão ser aprovado, banco de talentos e não selecionado.
aprovado = (
            f"Candidato: {nome}\n"
            f"Pontuação no teste: {pontuacao_teste}\n"
            f"Porcentagem de presença: {porcentagem_presenca}%\n"
            f"Resultado: Aprovado para a próxima etapa!"
           )

banco_de_talentos = (
            f"Candidato: {nome}\n"
            f"Pontuação no teste: {pontuacao_teste}\n"
            f"Porcentagem de presença: {porcentagem_presenca}%\n"
            f"Resultado: Classificado para o banco de talentos!"
            )
nao_selecionado = (
            f"Candidato: {nome}\n"
            f"Pontuação no teste: {pontuacao_teste}\n"
            f"Porcentagem de presença: {porcentagem_presenca}%\n"
            f"Resultado: Não selecionado!"
           )

#aqui iremos começar as condicionais.
if (pontuacao_teste >= 70 and porcentagem_presenca >= 75):
    print(aprovado)
elif (pontuacao_teste >= 50 and porcentagem_presenca >= 60):
    print (banco_de_talentos)
else:
    print (nao_selecionado)
