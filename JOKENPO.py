import random
from time import sleep
from turtle import Turtle

print("\033[1;33m-="*5, "Bom dia, seja bem vindo(a) ao nosso desafio!", "-="*5)
print()
print("          Jogue conosco um Jokenpô e se divirta bastante.")
print()

contador_vitorias = 0
contador_derrotas = 0
contador_empates = 0

resposta = True
while resposta:
    # Lista de opções do computador.
    lista_de_jogadas = ["PEDRA", "PAPEL", "TESOURA"] 
    computador = random.choice(lista_de_jogadas)
    print('\033[1;33m-=\033[m' * 33)
    #Escolha do jogador.
    jogador = input("\033[4;35mEscolha: PEDRA, PAPEL ou TESOURA -\033[m ").upper().strip() 
    
    while jogador not in lista_de_jogadas:
        print("Opção inválida. Tente novamente.")
        jogador = input("\033[4;35mEscolha: PEDRA, PAPEL ou TESOURA -\033[m ").upper().strip()
        
    print("\033[1;31mJO")
    sleep(1)
    print("\033[1;34mKEN")
    sleep(1)
    print("\033[1;32mPÔ")
    sleep(1)
    # Analise para saber quem venceu.
    if jogador == computador:
        print("\033[1;34mVocês escolheram o mesmo.")
        contador_empates += 1

    elif jogador == 'PEDRA':
        if computador == 'PAPEL':
            print("\033[1;4;31mVocê perdeu!\033[m\n\033[1;31mO computador escolheu {} e você {}.".format(computador, jogador))
            contador_derrotas += 1
        elif computador == 'TESOURA':
            print("\033[4;1;32mVocê ganhou!!\033[m\n\033[1;32mParabéns, você escolheu {} e o computador {}.".format(jogador, computador))
            contador_vitorias += 1

    elif jogador == 'PAPEL':
        if computador == 'PEDRA':
            print("\033[4;1;32mVocê ganhou!!\033[m\n\033[1;32mParabéns, você escolheu {} e o computador {}.".format(jogador, computador))
            contador_vitorias += 1
        elif computador == 'TESOURA':
            print("\033[1;4;31mVocê perdeu!\033[m\n\033[1;31mO computador escolheu {} e você {}.".format(computador, jogador))
            contador_derrotas += 1

    elif jogador == 'TESOURA':
        if computador == 'PEDRA':
            print("\033[1;4;31mVocê perdeu!\033[m\n\033[1;31mO computador escolheu {} e você {}.".format(computador, jogador))
            contador_derrotas += 1
        elif computador == 'PAPEL':
            print("\033[4;1;32mVocê ganhou!!\033[m\n\033[1;32mParabéns, você escolheu {} e o computador {}.".format(jogador, computador))
            contador_vitorias += 1
    # Para saber se ainda quer continuar jogando ou não.
    lista_de_resposta = ['S','N']
    r = ''
    while r not in lista_de_resposta:
        r = input('Quer jogar novamente?').upper()
        if r == 'N':
            resposta = False
        elif r == 'S':
            break
print('\033[1;33m-=\033[m' * 33)
# Contadores de vitorias, derrotas e empates.
if contador_vitorias != 0:
    print(f'\033[1;32mVocê venceu {contador_vitorias} vezes.\033[m')
if contador_derrotas != 0:
    print(f'\033[1;31mVocê perdeu {contador_derrotas} vezes.\033[m')
if contador_empates != 0:
    print(f'\033[1;34mVocê empatou {contador_empates} vezes.\033[m')
print('\033[1;33m-=\033[m' * 33)
print('\033[1;35mObrigado por jogar conosco.\nVolte Sempre')