lista = [1, 10]
try:
    arquivo = open('teste.txt', 'r')
    divisao = 10/2
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por zero (0)!')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritimética.')
except IndexError:
    print('Erro ao acessar um índice inválido da lista!')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}' .format(ex))
else:
    print('Executa quando não ocorre exceção!')
finally:
    print('Sempre executa.')
    print('Fechando o Arquivo')
    arquivo.close()