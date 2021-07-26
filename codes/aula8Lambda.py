contador_letras = lambda lista: [len(x) for x in lista]

lista = ['ney', 'marcos', 'lopes', 'brito']
print(contador_letras(lista))

soma = lambda a, b: a + b
subtracao = lambda a,b: a - b
print(soma(5,10))
print(subtracao(10,5))


calculadora ={
    'soma': lambda a,b: a+b,
    'subtracao': lambda a,b: a-b,
    'multiplicacao': lambda a,b: a*b,
    'divisao': lambda a,b: a/b,
}

print(type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
print(soma(1,5))