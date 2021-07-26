nota1 = int(input("Primeiro bimestre: "))
if nota1 > 10:
    nota1 = int(input("Você digitou errado. \nSegundo bimestre:"))
nota2 = int(input("Segundo bimestre: "))
if nota2 > 10:
    nota2 = int(input("Você digitou errado. \nTerceiro bimestre:"))
nota3 = int(input("Terceiro bimestre: "))
if nota3 > 10:
    nota3 = int(input("Você digitou errado. \nQuarto bimestre:"))
nota4 = int(input("Quarto bimestre: "))
if nota4 > 10:
    nota4 = int(input("Você digitou errado. \nPrimeiro bimestre:"))

media = (nota1+nota2+nota3+nota4)/4
print("Media: {}".format(media))

if not 5==5:
    print('afirmação verdadeira')
else:
    print('afirmação falsa')


if nota1 <= 10 and nota2 <= 10 and nota3 <= 10 and nota4 <= 10:
    print("Média: {}".format(media))
else:
    print('Foi informada alguma nota errada.')



a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))

resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or resto_b == 0:
    print("Foi digitador numero par".format(a))
else:
    print("Não foi digitado numero par!".format(a))


a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

if a > b and a > c:
    print("O maior valor é {}".format(a))
elif b > a and b > c:
    print("O maior numero é {}".format(b))
else:
    print("O maior numero é {}". format(c))

print("Final do programa")

