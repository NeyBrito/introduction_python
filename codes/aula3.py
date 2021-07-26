
nota = 0
np = 4
n = 0
controle = 0
while n < np:
    nota = int(input("{}º bimestre: ".format(n+1)))
    while nota > 10:
        nota = int(input("Você digitou errado. \n{} bimestre: ".format(n+1)))
    n+=1
    nota+=controle
    controle = nota
media = (nota) / 4
print("Media: {}".format(media))

resultado = 0
for x in range(1, 10):
    if x < 9:
        resultado += 1
print(resultado)

a = int(input('Entre com o número: '))
div = 0
for x in range(1, a+1):
	resto = a % x
	if resto == 0:
		div += 1

if div == 2 :
	print('número {} é primo'.format(a))
else:
	print('número {} não é primo'.format(a))


a = int(input('Digite um número: '))
while a % 2 != 0:
    a = int(input('Digite um número: '))

a = 100
range (1, a-5)

print(a)
for x in range(5):
    resultado = x

print(resultado)

# nota1 = int(input("Primeiro bimestre: "))
# while nota1 > 10:
#     nota1 = int(input("Você digitou errado. \nSegundo bimestre:"))
# nota2 = int(input("Segundo bimestre: "))
# while nota2 > 10:
#     nota2 = int(input("Você digitou errado. \nTerceiro bimestre:"))
# nota3 = int(input("Terceiro bimestre: "))
# while nota3 > 10:
#     nota3 = int(input("Você digitou errado. \nQuarto bimestre:"))
# nota4 = int(input("Quarto bimestre: "))
# while nota4 > 10:
#     nota4 = int(input("Você digitou errado. \nPrimeiro bimestre:"))
# media = (nota1+nota2+nota3+nota4)/4
# print("Media: {}".format(media))




# nota  =  int(input("Entre com uma nota: "))
# while nota > 10:
#     nota = int(input("Nota invalida. \nEntre com a nota correta: "))

# a = 0
# while a <= 10:
#     print(a)
#     a += 1





# # Verificando se uma sequencia de número é primo
# a = int(input("Digite um numero: "))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print("O númerdo {} é primeo!".format(num))
#     # else:
#     #     print("O número {} não é primo!".format(i))
#
#
# # for x in range(101):
# #     print(x)



