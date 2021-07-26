class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input("Entre com um numero de 0 a 10: "))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0.')
        break
    except ValueError:
        print('Valor inválido: Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)
class InputError(Exception):
    def __init__(self, message):
        self.message = message

nome = 'Adda'
while True:
    try:
        x = input('Digite um nome: ')
        if x == nome:
            break
        else:
            raise InputError('Nome inválido')
    except InputError as ex:
        print(ex)


bandas_metal = ['Iron Maiden', 'Angra', 'Slayer', 'Megadeth', 'Krisiun']
nova_banda = 'Caetano Veloso'
if nova_banda not in bandas_metal:
  raise InputError('{} não é metal!'.format(nova_banda))
print(nova_banda)

try:
  x = 0
  elementos = ['terra', 'ar', 'fogo', 'agua']
  elementos.pop(x)
except:
  print('Elemento não encontrado')
else:
  print('Elemento {} removido.'.format(x))
finally:
  print('Busca completa')

try:
    lista = [1, 2]
    print(lista[2])
except Exception:
    print('Ocorreu um erro desconhecido')
except IndexError:
    print('Não foi possível acessar o index pois ele não existe na lista')

try:
    divisao = 10 / 0
except ArithmeticError:
    erro = 'Houve um erro ao realizar uma operação aritmética'
except Exception:
    erro = 'Ocorreu um erro desconhecido'
else:
    erro = False
finally:
    if erro:
        print(erro)
    else:
        print(divisao)