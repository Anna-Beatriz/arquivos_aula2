#Faça um programa que simule um lançamento de dados. 
# Lance o dado 10 vezes e armazene os resultados em uma lista. 
# Depois, informe quantas vezes cada número foi sorteado.

import random

lista = []

for i in range(10):
    n = random.randint(1, 6)
    lista.append(n)

print(lista)