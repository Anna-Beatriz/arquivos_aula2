#Preencha uma lista com 10 números digitados pelo usuário e exiba:
#o maior número
#o menor número
#a média dos números
#todos os números menores que a média calculada
lista = []
for i in range(10):
    nums = int(input('Digite um número:'))
    lista.append(nums)

print(lista)

menor = min(lista)
print('Menor: ', menor)

maior = max(lista)
print('Maior: ', maior)

media = sum(lista) / len(lista)
print('Média:', media)

lista2 = []
for i in range(10):
    if lista[i] < media:
        print(lista[i])
