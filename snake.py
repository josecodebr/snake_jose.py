# Snake por joseanastacio
# Estudando python com ajuda do chatgpt
# projeto simple porem muito divertido de fazer para terminal
# Data: 16/05/2025 Vercao 1.2

import os
import time
import random
import msvcrt

# Configurações iniciais
largura = 40
altura = 20
velocidade_base = 0.15  # tempo inicial entre movimentos (segundos)
velocidade_min = 0.05   # velocidade máxima (menor delay)
velocidade = velocidade_base

# Variáveis do jogo
cobra = [(5, 5)]
direcao = (0, 1)  # começa indo pra direita
comida = (random.randint(1, altura - 2), random.randint(1, largura - 2))
pontuacao = 0
highscore = 0

def desenhar():
    os.system('cls')
    for y in range(altura):
        linha = ''
        for x in range(largura):
            if (y, x) == cobra[0]:
                #linha += '@'  # cabeça
                linha += '☺'  # cabeça
                
            elif (y, x) in cobra:
                linha += 'o'  # corpo
                
            elif (y, x) == comida:
                #linha += '*'  # comida
                linha += '♥'  # comida
            elif y == 0 or y == altura - 1 or x == 0 or x == largura - 1:
                linha += '▒'
            else:
                linha += ' '
        print(linha)
    print(f"Pontuação: {pontuacao}   Recorde: {highscore}")

def ler_tecla():
    global direcao
    if msvcrt.kbhit():
        tecla = msvcrt.getch()
        if tecla in [b'w', b'H'] and direcao != (1, 0):  # cima
            direcao = (-1, 0)
        elif tecla in [b's', b'P'] and direcao != (-1, 0):  # baixo
            direcao = (1, 0)
        elif tecla in [b'a', b'K'] and direcao != (0, 1):  # esquerda
            direcao = (0, -1)
        elif tecla in [b'd', b'M'] and direcao != (0, -1):  # direita
            direcao = (0, 1)

def mover():
    global comida, pontuacao, velocidade, highscore
    cabeca = cobra[0]
    nova = (cabeca[0] + direcao[0], cabeca[1] + direcao[1])

    # Colisão com parede ou corpo
    if nova in cobra or nova[0] == 0 or nova[0] == altura - 1 or nova[1] == 0 or nova[1] == largura - 1:
        return False

    cobra.insert(0, nova)

    if nova == comida:
        pontuacao += 1
        if pontuacao > highscore:
            highscore = pontuacao
        # aumenta a velocidade um pouco, com limite mínimo
        velocidade = max(velocidade_min, velocidade_base - pontuacao * 0.01)
        comida = (random.randint(1, altura - 2), random.randint(1, largura - 2))
    else:
        cobra.pop()

    return True

def menu():
    os.system('cls')
    print("=== Jogo da Cobrinha ===")
    print("Use W A S D ou setas para controlar.")
    print("Pressione qualquer tecla para começar...")
    msvcrt.getch()

# Executa o menu antes do jogo
menu()

# Loop principal
while True:
    desenhar()
    ler_tecla()
    if not mover():
        print("\nGame Over!")
        print(f"Sua pontuação final foi: {pontuacao}")
        print(f"Recorde atual: {highscore}")
        print("Pressione qualquer tecla para sair...")
        msvcrt.getch()
        break
    time.sleep(velocidade)
# ------ Fim do codigo ------
