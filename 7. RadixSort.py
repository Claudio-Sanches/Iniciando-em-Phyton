# Descrição   : Classificação método Radixsort
# Autor(a)    : Claudio Buzzolini Sanches
# Data atual  : 01/04/2021

import random


# import numpy as np

def TecleEnter():
    input("Tecle Enter")


def imprimir(Titulo):
    print("                        Vetor que está sendo Classificado na ordenação - ", Ordem)
    print(" ")
    print('   [', end="")
    for i in range(15):
        print(f'{pilha1[i]:5},', end="")
    print("]")
    print(" ")
    print(" ")
    print("                               Matriz de classificação Fase da ", Titulo)
    print("            _____   _____   _____   _____   _____   _____   _____   _____   _____   _____")
    for i in range(14, -1, -1):
        print("")
        print(f'{i:9}  ', end="")
        for j in range(10):
            if j > 8:
                if pilha00[i][j] == 0:
                    print("|     | ", end="")
                else:
                    print(f'|{pilha00[i][j]:5}| ', end="")
            else:
                if pilha00[i][j] == 0:
                    print("|     | ", end="")
                else:
                    print(f'|{pilha00[i][j]:5}| ', end="")
    print("")
    print("           |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____| |_____|")
    print("              0       1       2       3       4       5       6       7       8       9")
    print(" ")
    print("Vetor Topo[", end="")
    for i in range(10):
        print(f'{exibe[i]:4}   ,', end="")
    print("]")
    print(" ")
    print(" ")
    print("                         ==== Vetor já Classificado pela ", Titulo, " ==== ")
    print(" ")
    print("   [", end="")
    for i in range(15):
        print(f'{pilha2[i]:5},', end="")
    print("]")
    print(" ")
    print(" ")
    TecleEnter()
    inicializar()


def inicializar():
    global topo, exibe, pilha00, Conta, Conta1
    pilha00 = []
    for I in range(15):
        for j in range(10):
            pilha00.append([0] * 10)
    topo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    exibe = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Conta = 0
    Conta1 = 0


def Vet_para_Matriz(MODO):
    global topo, exibe, pilha00, x
    if MODO == 1:
        for i in range(15):
            x = pilha[i] % 10
            pilha00[topo[x]][x] = pilha[i]
            topo[x] = topo[x] + 1
        for i in range(10):
            exibe[i] = topo[i]
    if MODO == 2:
        for i in range(15):
            x = int(((pilha[i] - pilha[i] % 10) / 10) % 10)
            pilha00[topo[x]][x] = pilha[i]
            topo[x] = topo[x] + 1
        for i in range(10):
            exibe[i] = topo[i]
    if MODO == 3:
        for i in range(15):
            x = int(((pilha[i] - pilha[i] % 10) / 100) % 10)
            pilha00[topo[x]][x] = pilha[i]
            topo[x] = topo[x] + 1
        for i in range(10):
            exibe[i] = topo[i]
    if MODO == 4:
        for i in range(15):
            x = int(((pilha[i] - pilha[i] % 10) / 1000) % 10)
            pilha00[topo[x]][x] = pilha[i]
            topo[x] = topo[x] + 1
        for i in range(10):
            exibe[i] = topo[i]


def Matriz_para_Vetor(Cres_Decres):
    global topo, exibe, pilha00, pilha, Ordem, Conta
    Conta = 0
    if Cres_Decres == 2:
        Ordem = "Decrescente"
        for I in range(9, -1, -1):
            Conta1 = 0
            for j in range(topo[I]):
                pilha[Conta] = pilha00[Conta1][I]
                topo[I] = topo[I] - 1
                Conta = Conta + 1
                Conta1 = Conta1 + 1
    else:
        Ordem = "Crescente"
        for I in range(0, 10, 1):
            Conta1 = 0
            for j in range(topo[I]):
                pilha[Conta] = pilha00[Conta1][I]
                topo[I] = topo[I] - 1
                Conta = Conta + 1
                Conta1 = Conta1 + 1


pilha = []
pilha1 = []
pilha2 = []
pilha3 = []
topo = []
exibe = []
for i in range(15):
    pilha1.append(0)
    pilha2.append(0)
    pilha3.append(0)
pilha.append(3221)
pilha.append(1)
pilha.append(10)
pilha.append(9680)
pilha.append(577)
pilha.append(9420)
pilha.append(7)
pilha.append(5622)
pilha.append(4793)
pilha.append(2030)
pilha.append(3138)
pilha.append(82)
pilha.append(2599)
pilha.append(743)
pilha.append(4127)
Repete = "N"
while Repete == "N":
    print(" ")
    print("  === Rotina de classificação de vetores - Método RadixSort ===")
    print(" ")
    print("  Está pré-definido o seguinte vetor de 15 posições:")
    print(" ")
    print("   [", end="")
    for i in range(15):
        print(f'{pilha[i]:5},', end="")
    print("]")
    print(" ")
    print("  Deseja:")
    print(" ")
    print("  (U - Utilizar) esse vetor ")
    print(" ")
    print("  (R - Randomico) gerar novo vetor de forma Randomica de 0 a 2000 de 15 posições")
    print(" ")
    print("  (S - Sair) caso não deseje mais classificações")
    print(" ")
    Gerar = str(input("   Digite aqui (U ou R ou S)=> ").upper())
    if Gerar == "U":
        print(" ")
        print("  === Rotina de classificação de vetores - Método RadixSort ===")
        print(" ")
        print("  Vamos trabalhar com esse vetor de 15 posições:")
        print(" ")
        print("   [", end="")
        for i in range(15):
            print(f'{pilha[i]:5},', end="")
        print("]")
        print(" ")
        print("  Deseja a classificação em ordem (C - Crescente) ou (D - Decrescente) ")
        print(" ")
        OP_Ordem = str(input("  Digite aqui => ").upper())
        for i in range(15):
            pilha3[i] = pilha[i]
        if OP_Ordem == "C":
            inicializar()
            for w in range(1, 5):
                for i in range(15):
                    pilha1[i] = pilha[i]
                Vet_para_Matriz(w)
                Matriz_para_Vetor(1)
                for i in range(15):
                    pilha2[i] = pilha[i]
                if w == 1:
                    imprimir("Unidade")
                if w == 2:
                    imprimir("Dezena")
                if w == 3:
                    imprimir("Centena")
                if w == 4:
                    imprimir("Milhar")
            print(" ")
            print("  === Rotina de classificação de vetores - Método RadixSort ===")
            print(" ")
            print("  Vetor Original")
            print(" ")
            print("   [", end="")
            for i in range(15):
                print(f'{pilha3[i]:5},', end="")
            print("]")
            print(" ")
            print(" ")
            print("  Vetor Classificado em ordem Crescente ")
            print(" ")
            print("   [", end="")
            for i in range(15):
                print(f'{pilha[i]:5},', end="")
            print("]")
            print(" ")
            print(" ")
            TecleEnter()
        if OP_Ordem == "D":
            inicializar()
            for w in range(1, 5):
                for i in range(15):
                    pilha1[i] = pilha[i]
                Vet_para_Matriz(w)
                Matriz_para_Vetor(2)
                for i in range(15):
                    pilha2[i] = pilha[i]
                if w == 1:
                    imprimir("Unidade")
                if w == 2:
                    imprimir("Dezena")
                if w == 3:
                    imprimir("Centena")
                if w == 4:
                    imprimir("Milhar")
            print(" ")
            print("  === Rotina de classificação de vetores - Método RadixSort ===")
            print(" ")
            print("  Vetor Original")
            print(" ")
            print("   [", end="")
            for i in range(15):
                print(f'{pilha3[i]:5},', end="")
            print("]")
            print(" ")
            print(" ")
            print("  Vetor Classificado em ordem Decrescente ")
            print(" ")
            print("   [", end="")
            for i in range(15):
                print(f'{pilha[i]:5},', end="")
            print("]")
            print(" ")
            print(" ")
            TecleEnter()
    if Gerar == "R":
        for i in range(15):
            pilha[i] = random.randrange(1, 2500)
    if Gerar == "S":
        Repete = "S"
