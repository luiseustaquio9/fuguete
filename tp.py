import sys
import os
from time import sleep

#alterar para 36000 como diz o exercício
ALTITUDE_MAXIMA=999

altitude_atual=0
velo=float(input("Digite a velocidade em km/s: "))

#em caso de windows, alterar na linha abaixo: 'clear' para 'cls'
#os.system('cls')

passos_necessarios = int(ALTITUDE_MAXIMA / velo)
passo_atual = 0
linha=0

passo_atual=0

while altitude_atual <= ALTITUDE_MAXIMA:

    passo_atual = passo_atual + 1

    sleep(1)

    altitude_atual = altitude_atual + velo

    #os.system('cls')

    print(f"\t__________ORBITA__________      (tempo: {passo_atual}s  altitude: {altitude_atual:.1f}km )")

    #o proximo loop serve para "desenhar" o foguete

    for linha in reversed(range(passos_necessarios)):

        if(passo_atual > linha):
            print('\t\t|')
        else:
            print('\t\t.')

#nesse ponto, o primeiro loop terminou ou seja, o foguete chegou
print('\n\tFoguete em orbita!!! \o/')