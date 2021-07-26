a = int(input('Digite o 1º valor: \n'))
b = int(input('Digite o 2º valor: \n'))

soma = a + b
subtração = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b


print("Soma: {soma}; "
      "\nSubtração: {sub}; "
      "\nMultiplicação: {mult}; "
      "\nDivisao: {div}; "
      "\nResto: {res};".format(soma=soma,
                               sub=subtração,
                               mult=multiplicacao,
                               div=divisao,
                               res=resto))
#
# print(type(soma))
# print("Soma: " + str(soma))
# print("Multiplicação: "+ str(multiplicacao))
# print("Subtração: "+ str(subtração))
# print("Divisao: "+ str(divisao))
# print("Resto: "+ str(resto))
#
# x = '1'
# soma2 = int(x) + 1
# print("Soma: ", soma2)

