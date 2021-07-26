conjunto1 = {4, 8, 12, 16}
conjunto2 = {5, 10, 15, 20}

conjunto_uniao = conjunto1.union(conjunto2)
print(conjunto_uniao)
conjunto_intesecao = conjunto1.intersection(conjunto2)
conjunto_diferenca = conjunto1.difference(conjunto2)
conjunto_simetrico = conjunto1.symmetric_difference(conjunto2)

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)
# conjunto.add(5)
# conjunto.discard(2)

conjunto = {10, 20, 30, 40, 50}
conjunto.discard (40)
print(conjunto)

mariana = 2 # dona da casa
renato = 4
larissa = 2
rafael = 5
augusto = 1
rafaela = 3

dedos = {mariana, renato, larissa, rafael, augusto, rafaela}
participantes = len(dedos) #quantidade de participantes
somaDedos = sum(dedos) #soma dos valores de cada dedo
dedoapontadopara = 0
for x in range(somaDedos):
  if dedoapontadopara > participantes:
     dedoapontadopara = 0
  dedoapontadopara += 1
dedos = list(dedos) #converter dedos para arquivo tipo 'list'
print('No final o dedo foi apontado para {}.'.format(dedos[dedoapontadopara]))

conjunto = {1, 2, 2, 1, 4, 5}
print(conjunto)

conjunto_a = {1, 1, 3, 4, 5}
conjunto_b = {1, 3, 6}
conjunto_a.add(6)
conjunto_a.remove(1)
resultado = list(conjunto_a.intersection(conjunto_b))
print(resultado)

print(conjunto)

print(conjunto_intesecao)
print(conjunto_diferenca)
print(conjunto_simetrico)