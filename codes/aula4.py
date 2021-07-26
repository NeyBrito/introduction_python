lista = [1 ,3 ,4 ,7]
lista_animal = ['cachorro', 'gato', 'elefante','lobo', 'arara']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1,2,3,4,5,6,7)
print(tupla)

print(len(tupla))
print(len(lista_animal))

tupla_animal = tuple(lista_animal)
print(tupla_animal)

lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)
lista_animal.reverse()
print(lista_animal)

print(lista_animal[1])
print(sum(lista))
print(max(lista))
print(min(lista))

for x in lista_animal:
    print(x)
if 'lobo' in lista_animal:
    print("Tem lobo na lista")
else:
    print("Não tem lobo na lista")
    lista_animal.append('lobo')
    print("Foi incuido Lobo na lista. \n", lista_animal)

lista_animal.pop() #retira o ultimo da lista sem parametro
print(lista_animal)

lista = [3, 5, 7, 10, 11]
resultado = []
for x in lista:
    if x % 2 == 1:
        resultado.append(x)
print(resultado)