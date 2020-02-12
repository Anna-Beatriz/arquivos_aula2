#Preencha uma lista com 20 números aleatórios. A partir desta lista, 
# gere uma lista com os números pares e outra lista com os números ímpares.
import random

lista = []
listaImpar = []
listaPar = []

for i in range(20):
    n = random.randint(1, 100)
    lista.append(n)

    if lista[i] % 2 == 0:
        listaPar.append(lista[i])
    else:
        listaImpar.append(lista[i])

print(lista)
print(listaPar)
print(listaImpar)